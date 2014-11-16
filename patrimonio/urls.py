from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'controle.views.index'),
    url(r'^validar/$', 'controle.views.index'),
)
