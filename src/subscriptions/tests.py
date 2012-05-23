# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse


class SubscriptionUrlTest(TestCase):
    def test_get_subscribe_page(self):
        response = self.client.get(reverse('subscriptions:subscribe'))
        self.assertEquals(200, response.status_code)

    def test_get_success_page(self):
        response = self.client.get(reverse('subscriptions:success', args=[1]))
        self.assertEquals(200, response.status_code)


class SubscriptionModelTest(TestCase):
    # 1) O modelo deve ter os campos: name, cpf, email, phone, created_at
    # 2) O cpf deve ser único
    # 3) O email deve ser único
