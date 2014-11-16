from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'controle.views.index'),
    #url(r'^validar/$', 'controle.views.index'),
    url(r'^cadastroPatrimonio/$', 'controle.views.cadastroPatrimonio'),
    url(r'^salvar/$', 'salvar'),
    url(r'^apagar/(?P<pk>\d+)/$', 'apagar'),
)
