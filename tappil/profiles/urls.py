from django.conf.urls import patterns, url
from tappil.profiles.views import ProfileMatch

urlpatterns = patterns('',
    url(r'^match/$', ProfileMatch.as_view(), name='profile-match'),
)