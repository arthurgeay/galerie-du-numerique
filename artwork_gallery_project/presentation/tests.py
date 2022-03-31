from django.test import TestCase

from django.test import Client
from django.shortcuts import resolve_url


class PresentationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.presentation_url = resolve_url("presentation")

    def test_can_view_page(self):
        response = self.client.get(self.presentation_url)
        self.assertEqual(response.resolver_match.url_name, "presentation")


class InfosTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.infos_url = resolve_url("infos")

    def test_can_view_page(self):
        response = self.client.get(self.infos_url)
        self.assertEqual(response.resolver_match.url_name, "infos")


class AgreementTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.agreement_url = resolve_url("agreement")

    def test_can_view_page(self):
        response = self.client.get(self.agreement_url)
        self.assertEqual(response.resolver_match.url_name, "agreement")


class PolicyTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.policy_url = resolve_url("policy")

    def test_can_view_page(self):
        response = self.client.get(self.policy_url)
        self.assertEqual(response.resolver_match.url_name, "policy")
