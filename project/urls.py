from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin



api_patterns = patterns('',
    url(r'^profile/', include('tappil.profiles.urls')),
    url(r'^link/', include('tappil.links.urls')),
)

app_patterns = patterns('',
    url(r'^dn/', include(admin.site.urls)),
    url(r'^v1/', include(api_patterns)),
)


urlpatterns = patterns('',
    url(r'^%s' % settings.APP_PATH_PREFIX, include(app_patterns))
)