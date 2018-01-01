from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [

	url(r'^GeneMapperApp/', include('GeneMapperApp.urls', namespace='GeneMapperApp', app_name='GeneMapperApp')),
    # Examples:
    # url(r'^$', 'GeneMapper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
