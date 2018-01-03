from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.convert, name='converter'),
    url(r'^(?P<id_type>)', views.convert, name='smelly'),
]