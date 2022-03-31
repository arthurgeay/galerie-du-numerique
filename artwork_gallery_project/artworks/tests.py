from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.shortcuts import resolve_url
from django.contrib.auth.models import User

from artworks.models import Artist, Category, Artwork

from artworks.services.client import ApiClient, ApiClientException

from artworks.services.wikiart_client import WikiArtClient
import environ


class GalleryTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.gallery_url = reverse("gallery")
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        User.objects.create_user(
            username=self.user["username"], password=self.user["password"]
        )

    def test_cannot_view_gallery_page_without_user_logged(self):
        response = self.client.get(self.gallery_url, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_view_page_correctly_with_user_logged(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.gallery_url)
        self.assertEqual(response.resolver_match.url_name, "gallery")

    def test_can_filter_artworks_by_category(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        category = Category.objects.create(name="Category 1")
        category2 = Category.objects.create(name="Category 2")
        artist = Artist.objects.create(name="Artist 1")
        artist2 = Artist.objects.create(name="Artist 2")

        Artwork.objects.create(title="Artwork 1", category=category, artist=artist)
        Artwork.objects.create(title="Artwork 2", category=category2, artist=artist2)

        response = self.client.get(self.gallery_url, {"category": category.id})
        self.assertEqual(response.resolver_match.url_name, "gallery")
        self.assertContains(response, "Réinitialiser les filtres")
        self.assertContains(response, "Artwork 1")
        self.assertNotContains(response, "Artwork 2")

    def test_can_sort_artworks_by_asc(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.gallery_url, {"sort": "ASC"})
        self.assertEqual(response.resolver_match.url_name, "gallery")
        self.assertContains(response, "Réinitialiser les filtres")

    def test_can_sort_artworks_by_desc(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.gallery_url, {"sort": "DESC"})
        self.assertEqual(response.resolver_match.url_name, "gallery")
        self.assertContains(response, "Réinitialiser les filtres")

    def test_can_filter_and_sort_artworks(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        category = Category.objects.create(name="Category 1")
        category2 = Category.objects.create(name="Category 2")
        artist = Artist.objects.create(name="Artist 1")
        artist2 = Artist.objects.create(name="Artist 2")

        Artwork.objects.create(title="Artwork 1", category=category, artist=artist)
        Artwork.objects.create(title="Artwork 2", category=category2, artist=artist2)

        response = self.client.get(
            self.gallery_url, {"category": category.id, "sort": "ASC"}
        )
        self.assertEqual(response.resolver_match.url_name, "gallery")
        self.assertContains(response, "Réinitialiser les filtres")
        self.assertContains(response, "Artwork 1")
        self.assertNotContains(response, "Artwork 2")


class ArtworkTest(TestCase):
    def setUp(self):
        self.client = Client()
        artist = Artist.objects.create(name="Jane Doe")
        category = Category.objects.create(name="Paint")
        artwork = Artwork.objects.create(
            title="Test Artwork",
            description="Test Description",
            artist=artist,
            category=category,
        )

        self.artwork_url = resolve_url("artwork_detail", id=artwork.id)
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        User.objects.create_user(
            username=self.user["username"], password=self.user["password"]
        )

    def test_cannot_view_artwork_page_without_user_logged(self):
        response = self.client.get(self.artwork_url, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_view_artwork_page_with_user_logged(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.artwork_url)
        self.assertEqual(response.resolver_match.url_name, "artwork_detail")
        self.assertContains(response, "Test Artwork")

    def test_cannot_view_artwork_not_exist(self):
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(resolve_url("artwork_detail", id=9999))
        self.assertEqual(response.resolver_match.url_name, "artwork_detail")
        self.assertEqual(response.status_code, 404)


class ApiClientTest(TestCase):
    def setUp(self):
        self.client = ApiClient(api_host="https://api.test.com")

    def test_cannot_generate_uri_with_invalid_query_params(self):
        with self.assertRaises(ApiClientException):
            self.client.generate_uri("/items", "failed")

    def test_can_generate_uri_without_query_params(self):
        result = self.client.generate_uri("/items")
        self.assertEqual(result, "https://api.test.com/items")

    def test_can_generate_uri_with_query_param(self):
        result = self.client.generate_uri("/items", {"page": 1})
        self.assertEqual(result, "https://api.test.com/items?page=1")

    def test_can_generate_uri_with_many_query_param(self):
        result = self.client.generate_uri("/items", {"page": 1, "limit": 10})
        self.assertEqual(result, "https://api.test.com/items?page=1&limit=10")


class WikiArtClientTest(TestCase):
    def setUp(self):
        self.env = environ.Env()
        environ.Env.read_env()
        self.client = WikiArtClient(
            access_code=self.env("MEDIAWIKI_ACCESS_CODE"),
            secret_code=self.env("MEDIAWIKI_SECRET_CODE"),
        )

    def test_can_search_artwork(self):
        result = self.client.search_artwork("joconde")

        self.assertTrue("data" in result)
        self.assertTrue("paginationToken" in result)
        self.assertTrue("hasMore" in result)

    def test_can_get_artwork_by_id(self):
        result = self.client.get_artwork("57726fa4edc2cb3880bb2fed")

        self.assertTrue("description" in result)
        self.assertTrue("image" in result)
        self.assertTrue("completitionYear" in result)
        self.assertTrue("width" in result)
        self.assertTrue("height" in result)
        self.assertTrue("location" in result)

    def test_can_get_artist_by_url(self):
        result = self.client.get_artist("fernand-leger")

        self.assertTrue("image" in result)
        self.assertTrue("birthDayAsString" in result)
        self.assertTrue("deathDayAsString" in result)
