# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse


class SuccessViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('subscriptions:success', args=[1]))

    def test_get(self):
        "Visita /inscrica/1/ e retorna 200."
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        "Renderiza o template"
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

