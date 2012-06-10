# coding: utf-8
from django.test import TestCase

from ..forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def test_cpf_has_only_digits(self):
        u'CPF deve ter apenas dígitos.'
        form = self.make_and_validate_form(cpf='ABCDE000000')
        self.assertDictEqual(form.errors,
                             {'cpf': [u'O CPF deve conter apenas números']})

    def test_cpf_has_11_digits(self):
        u'CPF deve ter exatamente 11 dígitos.'
        form = self.make_and_validate_form(cpf='000000000012')
        self.assertDictEqual(form.errors,
                             {'cpf': [u'O CPF deve ter 11 dígitos']})

    def make_and_validate_form(self, **kwargs):
        data = dict(name='Henrique Bastos', email='henrique@bastos.net', cpf='00000000000', phone='21-96186180')
        data.update(kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
