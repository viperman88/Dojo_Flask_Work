from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^courses/add_course$', views.add_course),
    url(r'^courses/(?P<course_id>\d+)/remove$', views.remove),
    url(r'^courses/(?P<course_id>\d+)/delete$', views.delete)
]
