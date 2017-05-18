from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^barty$', views.index, name='index'),
<<<<<<< HEAD
    url(r'^david$', views.url_david, name='index')
=======
    url(r'^bortolotti$', views.bortolotti, name='bortolotti')
>>>>>>> 9236fac20c002ea47f278b92c2932f034190886a
]

