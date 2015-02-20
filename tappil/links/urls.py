from django.conf.urls import patterns, url
from tappil.links.views import Activation


urlpatterns = patterns('',
    url(r'^(?P<code>\w+)/$', Activation.as_view(), name='activation'),
)