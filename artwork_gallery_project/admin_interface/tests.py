from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.urls import reverse

from artworks.models import Category, Artist, Artwork


def create_artwork():
    category = Category.objects.create(name="Test Category")
    artist = Artist.objects.create(name="Test Artist")
    artwork = Artwork.objects.create(
        title="Test Artwork", category=category, artist=artist
    )
    return artwork


def generate_url(name, id):
    return reverse(name, kwargs={"id": id})


class AdminArtworkViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_artworks = reverse("view_artworks")
        self.user = {"username": "testuser", "password": "superPassw0rd"}

    def test_cannot_view_artworks_page_without_user_logged(self):
        response = self.client.get(self.view_artworks, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_view_artworks_page_without_admin_user_permissions(self):
        User.objects.create_user(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.view_artworks, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_view_artworks_page_with_admin_user_permissions(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.view_artworks)
        self.assertEqual(response.resolver_match.url_name, "view_artworks")

    def test_can_view_artworks_page_without_artworks(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.view_artworks)
        self.assertContains(
            response, "Il semblerait qu'il n'y ait aucune oeuvre pour le moment."
        )

    def test_can_view_artworks_page_with_artworks(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        artwork = create_artwork()

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )
        response = self.client.get(self.view_artworks)

        self.assertContains(response, artwork.title)
        self.assertContains(response, artwork.artist.name)
        self.assertEqual(len(response.context["artworks"]), 1)


class AdminCreateArtworkTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_artwork = reverse("create_artwork")
        self.user = {"username": "testuser", "password": "superPassw0rd"}

    def test_cannot_create_artwork_without_user_logged(self):
        response = self.client.post(self.create_artwork, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_create_artwork_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(self.create_artwork, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_create_same_artwork_for_same_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        artwork = create_artwork()
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            self.create_artwork,
            {
                "title": artwork.title,
                "category": artwork.category.id,
                "artist": artwork.artist.id,
            },
            follow=True,
        )

        self.assertContains(
            response, "Un objet Artwork avec ces champs Title et Artist existe déjà."
        )

    def test_can_create_same_artwork_for_another_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        artwork = create_artwork()
        artist = Artist.objects.create(name="Test Artist 2")

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            self.create_artwork,
            {
                "title": artwork.title,
                "category": artwork.category.id,
                "artist": artist.id,
            },
            follow=True,
        )

        self.assertEqual(response.resolver_match.url_name, "view_artworks")
        self.assertContains(response, "{} a bien été sauvegardé.".format(artwork.title))

    def test_can_create_artwork_with_admin_permissions(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        category = Category.objects.create(name="Test Category")
        artist = Artist.objects.create(name="Test Artist")

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            self.create_artwork,
            {
                "title": "Test Artwork",
                "category": category.id,
                "artist": artist.id,
            },
            follow=True,
        )

        self.assertEqual(response.resolver_match.url_name, "view_artworks")
        self.assertContains(response, "Test Artwork a bien été sauvegardé.")


class AdminUpdateArtworkTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        self.artwork = create_artwork()

    def test_cannot_update_artwork_without_user_logged(self):
        response = self.client.post(
            generate_url("edit_artwork", self.artwork.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_update_artwork_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("edit_artwork", self.artwork.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_update_artwork_not_found(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("edit_artwork", 10000), {}, follow=True
        )

        self.assertEqual(response.status_code, 404)

    def test_can_update_artwork(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        artist = Artist.objects.create(name="Test Artist 2")
        category = Category.objects.create(name="Test Category 2")

        response = self.client.post(
            generate_url("edit_artwork", self.artwork.id),
            {
                "title": "Test Artwork Updated",
                "description": "Test Description Updated",
                "category": category.id,
                "artist": artist.id,
                "image": "",
                "released_at": "2020",
                "width": "100",
                "height": "100",
                "location": "Test Location Updated",
            },
            follow=True,
        )

        self.assertEqual(response.resolver_match.url_name, "view_artworks")
        self.assertContains(response, "Test Artwork Updated a bien été modifié")


class AdminDeleteArtworkTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        self.artwork = create_artwork()

    def test_cannot_delete_artwork_without_user_logged(self):
        response = self.client.post(
            generate_url("delete_artwork", self.artwork.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_delete_artwork_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artwork", self.artwork.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_delete_artwork_not_found(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artwork", 10000), {}, follow=True
        )

        self.assertEqual(response.status_code, 404)

    def test_can_delete_artwork(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artwork", self.artwork.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "view_artworks")
        self.assertContains(
            response, "{} a bien été supprimé".format(self.artwork.title)
        )


class AdminArtistViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        self.view_artists = reverse("view_artists")

    def test_cannot_view_artists_without_user_logged(self):
        response = self.client.get(self.view_artists, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_view_artists_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.view_artists, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_view_artists_page_without_artists(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.get(self.view_artists)
        self.assertContains(
            response, "Il semblerait qu'il n'y ait aucun artiste pour le moment."
        )

    def test_can_view_artists_page_with_artists(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        artist = Artist.objects.create(name="Test Artist")

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )
        response = self.client.get(self.view_artists)

        self.assertContains(response, artist.name)
        self.assertEqual(len(response.context["artists"]), 1)


class AdminCreateArtistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_artist = reverse("create_artist")
        self.user = {"username": "testuser", "password": "superPassw0rd"}

    def test_cannot_create_artist_without_user_logged(self):
        response = self.client.post(self.create_artist, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_create_artist_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(self.create_artist, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_create_same_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        artist = Artist.objects.create(name="Test Artist")

        response = self.client.post(
            self.create_artist,
            {
                "name": artist.name,
            },
            follow=True,
        )

        self.assertContains(response, "Un objet Artist avec ce champ Name existe déjà.")

    def test_can_create_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            self.create_artist,
            {"name": "Test Artwork", "birthday": "1990-01-01"},
            follow=True,
        )

        self.assertEqual(response.resolver_match.url_name, "view_artists")
        self.assertContains(response, "Test Artwork")


class AdminUpdateArtistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        self.artist = Artist.objects.create(name="Test Artist")

    def test_cannot_update_artist_without_user_logged(self):
        response = self.client.post(
            generate_url("edit_artist", self.artist.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_update_artist_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("edit_artist", self.artist.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_update_artist_not_found(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(generate_url("edit_artist", 10000), {}, follow=True)

        self.assertEqual(response.status_code, 404)

    def test_can_update_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("edit_artist", self.artist.id),
            {
                "name": "Test Artist Updated",
            },
            follow=True,
        )

        self.assertEqual(response.resolver_match.url_name, "view_artists")
        self.assertContains(response, "Test Artist")


class AdminDeleteArtistTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {"username": "testuser", "password": "superPassw0rd"}
        self.artist = Artist.objects.create(name="Test Artist")

    def test_cannot_delete_artist_without_user_logged(self):
        response = self.client.post(
            generate_url("delete_artist", self.artist.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_delete_artist_without_admin_permissions(self):
        User.objects.create_user(self.user["username"], self.user["password"])
        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artist", self.artist.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "login")

    def test_cannot_delete_artist_not_found(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artist", 10000), {}, follow=True
        )

        self.assertEqual(response.status_code, 404)

    def test_can_delete_artist(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(
            username=self.user["username"], password=self.user["password"]
        )

        response = self.client.post(
            generate_url("delete_artist", self.artist.id), {}, follow=True
        )

        self.assertEqual(response.resolver_match.url_name, "view_artists")
        self.assertContains(response, "{} a bien été supprimé".format(self.artist.name))
