from django.conf.urls import url
from tappil.links.views import Activation


urlpatterns = [
    url(r'^(?P<code>\w+)/$', Activation.as_view(), name='activation'),
]