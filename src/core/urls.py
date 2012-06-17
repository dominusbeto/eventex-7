# coding: utf-8
from django.conf.urls import patterns, include, url
from .views import SpeakerDetail
from .views import TalkDetail

urlpatterns = patterns('src.core.views',
    url(r'^palestrantes/(?P<slug>[\w-]+)/$', SpeakerDetail.as_view(), name='speaker_detail'),
    url(r'^palestras/$', 'talks', name='talks'),
    url(r'^palestras/(?P<pk>\d+)$', TalkDetail.as_view(), name='talk_detail'),
)
