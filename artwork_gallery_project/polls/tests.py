from django.test import TestCase
from django.test import Client
from django.shortcuts import resolve_url

from artworks.models import Artist, Category, Artwork
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class PollsTest(TestCase):
    def setUp(self):
        self.client = Client()
        artist = Artist.objects.create(name="Jane Doe")
        category = Category.objects.create(name="Paint")
        self.artwork = Artwork.objects.create(
            title="Test Artwork",
            description="Test Description",
            artist=artist,
            category=category,
        )

        self.artwork_vote_url = resolve_url("add_vote", id=self.artwork.id)

        self.user = User.objects.create_user(
            username="testuser", password="superPassw0rd"
        )
        customer_group = Group.objects.get(name="customers")
        self.user.groups.add(customer_group)

    def test_cannot_vote_without_user_logged(self):
        response = self.client.post(self.artwork_vote_url, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "login")

    def test_can_vote_with_user_logged(self):
        self.client.force_login(self.user)

        response = self.client.post(self.artwork_vote_url, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "artwork_detail")

        self.assertEqual(self.artwork.votes.count(), 1)

    def test_cannot_vote_twice_for_same_artwork(self):
        self.client.force_login(self.user)

        response = self.client.post(self.artwork_vote_url, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "artwork_detail")

        response = self.client.post(self.artwork_vote_url, {}, follow=True)
        self.assertEqual(response.resolver_match.url_name, "artwork_detail")

        self.assertContains(response, "Vous avez déjà voté pour cette oeuvre.")
