
from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new),
    url(r'^create', views.create),
    url(r'^(?P<number>\d+)/show', views.show),
    url(r'^(?P<number>\d+)/delete', views.destroy),
    url(r'^edit', views.edit)
]
