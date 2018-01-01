from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.geneinfo_list, name='GeneInfo_list'),
	]