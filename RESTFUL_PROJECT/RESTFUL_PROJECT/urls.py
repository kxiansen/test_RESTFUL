from django.conf.urls import include, url
from django.contrib import admin
import api

urlpatterns = [
    # Examples:
    # url(r'^$', 'RESTFUL_PROJECT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('api.urls',namespace='api')),
]
