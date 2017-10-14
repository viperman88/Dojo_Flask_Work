from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all_surveys', views.all_surveys),
    url(r'^new_surveys', views.new_surveys)
]
