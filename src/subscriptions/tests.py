# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Subscription


class SubscriptionUrlTest(TestCase):
    def test_get_subscribe_page(self):
        response = self.client.get(reverse('subscriptions:subscribe'))
        self.assertEquals(200, response.status_code)

    def test_get_success_page(self):
        response = self.client.get(reverse('subscriptions:success', args=[1]))
        self.assertEquals(200, response.status_code)


class SubscriptionModelTest(TestCase):
    def test_create(self):
        "O modelo deve ter os campos: name, cpf, email, phone, created_at."

        s = Subscription.objects.create(
            name='Henrique Bastos',
            cpf='012345678901',
            email='henrique@bastos.net',
            phone='21-96186180'
        )
        self.assertEquals(s.id, 1)

    # 2) O cpf deve ser único
    # 3) O email deve ser único
