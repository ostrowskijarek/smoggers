from django.conf.urls import url
from showmap.views import ShowMap
urlpatterns = [
    url(r'^$', ShowMap.as_view()),
]