from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.shortcuts import resolve_url
from django.contrib.auth.models import User

from artworks.models import Artist, Category, Artwork


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
