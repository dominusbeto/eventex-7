# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from src.core.models import Speaker


def homepage(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    return direct_to_template(request, 'core/speaker_detail.html', {'speaker': speaker})