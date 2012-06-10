# coding: utf-8
from mock import Mock
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
