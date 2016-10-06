from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^crear$', views.crear, name='crear'),
    # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),

]
