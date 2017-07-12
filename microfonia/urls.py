from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^videos$', views.videos, name='videos'),
    url(r'^quemsomos$', views.aboutus, name='quemsomos'),
    url(r'^contato$', views.contact, name='contato'),
    url(r'^(?P<seriename>.+)/(?P<seasonnum>\d+)_(?P<episodenum>\d+)$', views.descricao, name='descricao'),
    url(r'^$', views.home, name='home')
]
	