from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^money$', views.money),
    url(r'^you_won$', views.you_won)
]
