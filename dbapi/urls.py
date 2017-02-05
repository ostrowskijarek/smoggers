from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^get_points/$', views.get_points, name='get_points'),
    url(r'^get_containers/$', views.get_containers, name='get_containers'),
    url(r'^set_point/$', views.set_point, name='set_point'),
]