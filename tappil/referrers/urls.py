from django.conf.urls import patterns, url
from tappil.profiles.views import ProfileMatch
from tappil.referrers.views import ReferrerForIp


urlpatterns = [
    url(r'^for-ip/$', ReferrerForIp.as_view(), name=ReferrerForIp.URL_NAME),
]
