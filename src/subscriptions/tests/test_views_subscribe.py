# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

from ..models import Subscription
from ..forms import SubscriptionForm


class SubscribeViewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('subscriptions:subscribe'))

    def test_get(self):
        "Ao visitar /inscricao/ a página de inscrição é exibida."
        self.assertEquals(200, self.resp.status_code)

    def test_use_template(self):
        "O corpo da resposta deve conter a renderização de um template."
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_form.html')

    def test_has_form(self):
        "A resposta deve conter o formulário de inscrição"
        self.assertIsInstance(self.resp.context['form'], SubscriptionForm)

    def test_form_has_fields(self):
        "O formulário de deve conter campos: name, email, cpf e phone."
        form = self.resp.context['form']
        self.assertItemsEqual(['name', 'email', 'cpf', 'phone'], form.fields)

    def test_html(self):
        "O html deve conter os campos do formulário"
        self.assertContains(self.resp, 'form')
        self.assertContains(self.resp, 'input', 6)
        self.assertContains(self.resp, 'type="text"', 4)
        self.assertContains(self.resp, 'submit')


class SubscribeViewPostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='00000000000',
                    email='henrique@bastos.net', phone='21-96186180')
        self.resp = self.client.post(reverse('subscriptions:subscribe'), data)

    def test_post(self):
        "Post deve redirecionar para página de sucesso."
        self.assertRedirects(self.resp,
                             reverse('subscriptions:success', args=[1]))

    def test_save(self):
        "Post deve salvar Subscription no banco."
        self.assertTrue(Subscription.objects.exists())

    def test_email_sent(self):
        "Post deve notificar visitante por email."
        self.assertEqual(1, len(mail.outbox))


class SubscribeViewInvalidPostTest(TestCase):
    def setUp(self):
        data = dict(name='Henrique Bastos', cpf='000000000001',
                    email='henrique@bastos.net', phone='21-96186180')
        self.resp = self.client.post(reverse('subscriptions:subscribe'), data)

    def test_show_page(self):
        "Post inválido não deve redirecionar."
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        "Form deve conter erros."
        self.assertTrue(self.resp.context['form'].errors)

    def test_must_not_save(self):
        "Dados não devem ser salvos."
        self.assertFalse(Subscription.objects.exists())

