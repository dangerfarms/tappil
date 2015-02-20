from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('tappil.profiles.urls')),
    url(r'^link/', include('tappil.profiles.urls')),
)