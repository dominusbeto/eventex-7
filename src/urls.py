from django.conf.urls import patterns, include, url
from src.core.views import Homepage

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('src',
    url(r'^$', Homepage.as_view(), name='homepage'),
    url(r'^inscricao/', include('src.subscriptions.urls', namespace='subscriptions')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('src.core.urls', namespace='core')),
)
