# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

from .models import Subscription


def CpfValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'O CPF deve conter apenas números'))
    if len(value) != 11:
        raise ValidationError(_(u'O CPF deve ter 11 dígitos'))


class SubscriptionForm(forms.ModelForm):
    cpf = forms.CharField(label=_('CPF'), validators=[CpfValidator])
    class Meta:
        model = Subscription
        exclude = ('paid',)