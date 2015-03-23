from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^v1/admin/', include(admin.site.urls)),
    url(r'^v1/profile/', include('tappil.profiles.urls')),
    url(r'^v1/link/', include('tappil.links.urls')),
)
