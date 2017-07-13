from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^videos$', views.videos, name='videos'),
   	url(r'^(?P<seriename>.+)/(?P<seasonnum>\d+)_(?P<episodenum>\d+)$', views.descricao, name='descricao'),
   	url(r'^$', views.home, name='home'),
   	url(r'^series$', views.series, name='series')
]
