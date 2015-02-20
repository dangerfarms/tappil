from django.conf.urls import patterns, include, url
from django.contrib import admin
from tappil.links.views import Activation

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', include('tappil.profiles.urls')),
    url(r'^(?P<code>\w+)/$', Activation.as_view(), name='activation'),
)
