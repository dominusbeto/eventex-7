# coding: utf-8
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.core.urlresolvers import reverse

from .forms import SubscriptionForm


def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return direct_to_template(request, 'subscriptions/subscription_form.html',
                              {'form': form})

    subscription = form.save()

    return HttpResponseRedirect(reverse('subscriptions:success',
                                        args=[subscription.pk]))


def new(request):
    return direct_to_template(request, 'subscriptions/subscription_form.html',
                              {'form': SubscriptionForm()})


def success(request, pk):
    return HttpResponse()
