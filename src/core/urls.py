# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import SpeakerDetail

urlpatterns = patterns('src.core.views',
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetail.as_view(), name='speaker_detail'),
    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestras/(\d+)$', 'talk_detail', name='talk_detail'),
)
