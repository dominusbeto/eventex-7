# coding: utf-8
from django.contrib.auth.models import User
from mock import Mock
from django.core.urlresolvers import reverse
from django.test import TestCase

from ..admin import SubscriptionAdmin, Subscription, admin


class CustomActionTest(TestCase):
    def setUp(self):
        Subscription.objects.create(name='Henrique Bastos', cpf='012345678901',
                                    email='henrique@bastos.net', phone='21-96186180')

        self.modeladmin = SubscriptionAdmin(Subscription, admin.site)
        # action!
        self.modeladmin.mark_as_paid(Mock(), Subscription.objects.all())

    def test_update(self):
        'Dados devem ser atualizados como pago de acordo com o Queryset.'
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())


class ExportSubscriptionViewTest(TestCase):
    def setUp(self):
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        assert self.client.login(username='admin', password='admin')
        self.resp = self.client.get(reverse('admin:export_subscriptions'))

    def test_get(self):
        u'Sucesso ao acessar url de download do arquivo csv.'
        self.assertEqual(200, self.resp.status_code)

    def test_content_type(self):
        u'Content type deve ser text/csv.'
        self.assertEqual('text/csv', self.resp['Content-Type'])

    def test_attachment(self):
        u'Header indicando ao browser que a resposta é um arquivo a ser salvo'
        self.assertTrue('attachment;' in self.resp['Content-Disposition'])


class ExportSubscriptionsNotFound(TestCase):
    def test_404(self):
        u'Login é exigido para download do csv'
        # Quando o usuário não está autenticado
        # o Admin response 200 e renderiza o html de login.
        response = self.client.get(reverse('admin:export_subscriptions'))
        self.assertTemplateUsed(response, 'admin/login.html')
