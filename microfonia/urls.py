from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^videos$', views.videos, name='videos'),
   	url(r'^(?P<seriename>.+)/(?P<seasonnum>\d+)_(?P<episodenum>\d+)$', views.descricao, name='descricao'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
