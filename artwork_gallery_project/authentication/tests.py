from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("signup")

        self.user = {
            "username": "JOhn",
            "email": "john@doe.com",
            "password1": "mysupers3cretPassw0rd",
            "password2": "mysupers3cretPassw0rd",
        }

        self.user_email_invalid = {
            "username": "JOhn",
            "email": "johnoe.com",
            "password1": "mysupers3cretPassw0rd",
            "password2": "mysupers3cretPassw0rd",
        }

        self.user_short_password = {
            "username": "JOhn",
            "email": "johnoe.com",
            "password1": "e",
            "password2": "e",
        }

        self.user_not_same_password = {
            "username": "JOhn",
            "email": "johnoe.com",
            "password1": "myFirstPassw0rd44",
            "password2": "myOtherPassw0rd44",
        }

    def test_can_view_page_correctly(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)

    def test_cannot_register_user_with_existing_username(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user)

        self.assertContains(response, "Un utilisateur avec ce nom existe déjà.")

    def test_cannot_register_user_with_email_invalid(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_email_invalid)

        self.assertContains(response, "Saisissez une adresse de courriel valide.")

    def test_cannot_register_user_with_short_password(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_short_password)

        self.assertContains(
            response,
            "Ce mot de passe est trop court. Il doit contenir au minimum 8 caractères.",
        )

    def test_cannot_register_user_with_not_same_password(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_not_same_password)

        self.assertContains(response, "Les deux mots de passe ne correspondent pas.")

    def test_can_register_user(self):
        response = self.client.post(self.register_url, self.user, follow=True)

        self.assertTrue(response.context["user"].is_authenticated)
        self.assertEqual(response.resolver_match.url_name, "gallery")


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse("signup")
        self.login_url = reverse("login")
        self.user = {
            "username": "JOhn",
            "email": "john@doe.com",
            "password1": "mysupers3cretPassw0rd",
            "password2": "mysupers3cretPassw0rd",
        }

    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_cannot_login_user_with_bad_credentials(self):
        response = self.client.post(
            self.login_url,
            {"username": self.user["username"], "password": self.user["password1"]},
        )
        self.assertContains(
            response,
            "Saisissez un nom d’utilisateur et un mot de passe valides. Remarquez que chacun de ces champs est sensible à la casse (différenciation des majuscules/minuscules).",
        )

    def test_can_login_user(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(
            self.login_url,
            {"username": self.user["username"], "password": self.user["password1"]},
            follow=True,
        )

        self.assertTrue(response.context["user"].is_authenticated)
        self.assertEqual(response.resolver_match.url_name, "gallery")


class LogoutTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", password="superPassw0rd"
        )
        customer_group = Group.objects.get(name="customers")
        self.user.groups.add(customer_group)

    def test_can_logout_user(self):
        self.client.login(username="testuser", password="superPassw0rd")
        response = self.client.get(reverse("logout"), follow=True)

        self.assertFalse(response.context["user"].is_authenticated)
        self.assertEqual(response.resolver_match.url_name, "login")
