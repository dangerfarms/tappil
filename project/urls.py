from django.conf.urls import patterns, include, url
from django.contrib import admin
from tappil.activations.views import Activation

urlpatterns = patterns('',
    url(r'^(?P<code>\w+)/$', Activation.as_view(), name='activation'),
    url(r'^admin/', include(admin.site.urls)),
)
