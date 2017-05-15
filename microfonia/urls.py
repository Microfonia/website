from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^barty$', views.index, name='index'),
    url(r'^bortolotti$', views.bortolotti, name='bortolotti')
]
