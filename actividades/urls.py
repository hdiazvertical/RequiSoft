from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^crear$', views.crear, name='crear'),
    url(r'^resultado$', views.resultado, name='resultado'),
]
