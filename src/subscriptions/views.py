# coding: utf-8
from django.http import HttpResponse
from django.views.generic.simple import direct_to_template

from .forms import SubscriptionForm


def subscribe(request):
    return direct_to_template(request, 'subscriptions/subscription_form.html',
                              {'form': SubscriptionForm()})


def success(request, pk):
    return HttpResponse()
