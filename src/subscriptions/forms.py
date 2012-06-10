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

    def clean(self):
        super(SubscriptionForm, self).clean()

        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise forms.ValidationError(
                _(u'Informe seu e-mail ou telefone.'))
        return self.cleaned_data
