from urlparse import urlparse
from django.core.exceptions import DisallowedRedirect
from django.http import HttpResponse
from django.utils.encoding import force_text, iri_to_uri


class DeepLinkRedirect(HttpResponse):
    status_code = 302
    allowed_schemes = ['pinseekerz',]

    def __init__(self, redirect_to, *args, **kwargs):
        parsed = urlparse(force_text(redirect_to))
        if parsed.scheme and parsed.scheme not in self.allowed_schemes:
            raise DisallowedRedirect("Unsafe redirect to URL with protocol '%s'" % parsed.scheme)
        super(DeepLinkRedirect, self).__init__(*args, **kwargs)
        self['Location'] = iri_to_uri(redirect_to)

    url = property(lambda self: self['Location'])