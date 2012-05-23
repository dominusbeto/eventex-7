# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse

from ..models import Subscription


class SuccessViewTest(TestCase):
    def setUp(self):
        s = Subscription.objects.create(name='Henrique Bastos', cpf='00000000000',
                                        email='henrique@bastos.net', phone='21-96186180')
        self.resp = self.client.get(reverse('subscriptions:success', args=[s.pk]))

    def test_get(self):
        "Visita /inscrica/1/ e retorna 200."
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        "Renderiza o template"
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        "Verifica instância de subscription no contexto."
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        self.assertContains(self.resp, 'Henrique Bastos')

class SuccessViewNotFound(TestCase):
    def test_not_found(self):
        response = self.client.get(reverse('subscriptions:success', args=[0]))
        self.assertEqual(404, response.status_code)
