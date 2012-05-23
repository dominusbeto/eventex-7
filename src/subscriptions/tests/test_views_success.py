# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse


class SuccessViewTest(TestCase):
    def test_get(self):
        "Visita /inscrica/1/ e retorna 200."
        response = self.client.get(reverse('subscriptions:success', args=[1]))
        self.assertEquals(200, response.status_code)

    # verifica template
