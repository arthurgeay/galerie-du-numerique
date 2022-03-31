from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User

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

        self.client.login(username=self.user["username"], password=self.user["password"])

        response = self.client.get(self.view_artworks, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_view_artworks_page_with_admin_user_permissions(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(username=self.user["username"], password=self.user["password"])

        response = self.client.get(self.view_artworks, follow=True)
        self.assertEqual(response.resolver_match.url_name, "view_artworks")

    def test_can_view_artworks_page_without_artworks(self):
        User.objects.create_superuser(
            username=self.user["username"], password=self.user["password"]
        )

        self.client.login(username=self.user["username"], password=self.user["password"])

        response = self.client.get(self.view_artworks, follow=True)
        self.assertContains(response, "Il semblerait qu'il n'y ait aucune oeuvre de disponible pour le moment.")
