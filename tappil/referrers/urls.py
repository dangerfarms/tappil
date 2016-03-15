from django.conf.urls import url

from tappil.referrers.views import ReferrerForIp


urlpatterns = [
    url(r'^for-ip/$', ReferrerForIp.as_view(), name=ReferrerForIp.URL_NAME),
]
