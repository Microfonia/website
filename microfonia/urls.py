from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^videos$', views.videos, name='videos'),
    url(r'^descricao$', views.descricao, name='descricao'),
    url(r'^(?P<episode_id>[0-9]+)/$', views.episodio, name="episodio")
]
