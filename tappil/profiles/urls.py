from django.conf.urls import url
from tappil.profiles.views import ProfileMatch

urlpatterns = [
    url(r'^match/$', ProfileMatch.as_view(), name='profile-match'),
]
