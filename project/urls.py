from django.conf.urls import patterns, include, url
from django.contrib import admin


api_patterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('tappil.profiles.urls')),
    url(r'^link/', include('tappil.links.urls')),
)

urlpatterns = patterns(
    url(r'^v1/', include(api_patterns)),
)