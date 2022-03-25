from django.test import TestCase
from django.test import Client
from django.urls import reverse

class RegisterTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('signup')

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

    def test_can_register_user_with_existing_username(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user)

        self.assertContains(response, 'Un utilisateur avec ce nom existe déjà.')

    def test_can_register_user_with_email_invalid(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_email_invalid)

        self.assertContains(response, 'Saisissez une adresse de courriel valide.')

    def test_can_register_user_with_short_password(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_short_password)

        self.assertContains(response, 'Ce mot de passe est trop court. Il doit contenir au minimum 8 caractères.')

    def test_can_register_user_with_not_same_password(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(self.register_url, self.user_not_same_password)

        self.assertContains(response, 'Les deux mots de passe ne correspondent pas.')

    def test_can_register_user(self):
        response = self.client.post(
            self.register_url,
            self.user,
            follow=True
        )

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.resolver_match.url_name, 'gallery')


class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('signup')
        self.login_url = reverse('login')
        self.user = {
            "username": "JOhn",
            "email": "john@doe.com",
            "password1": "mysupers3cretPassw0rd",
            "password2": "mysupers3cretPassw0rd",
        }

    def test_can_view_page_correctly(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)

    def test_can_login_user_with_bad_credentials(self):
        response = self.client.post(self.login_url, {"username": self.user['username'], "password": self.user['password1']})
        self.assertContains(response, 'Identifiants invalides')

    def test_can_login_user(self):
        self.client.post(self.register_url, self.user)
        response = self.client.post(
            self.login_url,
            {"username": self.user['username'], "password": self.user['password1']},
            follow=True
        )

        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.resolver_match.url_name, 'gallery')

