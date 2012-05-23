# coding: utf-8
from django.test import TestCase


class SubscriptionUrlTest(TestCase):
    def test_get_subscribe_page(self):
        response = self.client.get('/inscricao/')
        self.assertEquals(200, response.status_code)

    def test_get_success_page(self):
        response = self.client.get('/inscricao/1/')
        self.assertEquals(200, response.status_code)
