from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^videos$', views.videos, name='videos'),
    url(r'^descricao$', views.descricao, name='descricao'),
    url(r'^quemsomos$', views.aboutus, name='quemsomos'),
    url(r'^contato$', views.contact, name='contato'),
]
	