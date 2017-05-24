from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^barty$', views.index, name='index'),
    url(r'^videos$', views.videos, name='index'),
    url(r'^descricao$', views.descricao, name='bortolotti')
]
