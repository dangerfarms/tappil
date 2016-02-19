from django.conf.urls import include, url
from django.contrib import admin

api_patterns = [
    url(r'^profile/', include('tappil.profiles.urls')),
    url(r'^link/', include('tappil.links.urls')),
]

urlpatterns = [
    url(r'^dn/', include(admin.site.urls)),
    url(r'^v1/', include(api_patterns)),
]