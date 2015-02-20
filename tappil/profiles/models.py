from django.db import models
from jsonfield.fields import JSONField
from tappil.links.models import Link


class Profile(models.Model):

    ip = models.IPAddressField()
    device_family = models.TextField()
    device_os = models.TextField()
    device_version = models.TextField()
    uuid = models.TextField(unique=True, null=True)

    link = models.ForeignKey(Link, related_name='profiles')

    meta_data = JSONField()

    installed_on = models.DateTimeField(null=True)

    # port REMOTE_PORT
    # language_  'HTTP_ACCEPT_LANGUAGE': 'en-GB,en;q=0.8,en-US;q=0.6,hu;q=0.4',
    # 'HTTP_X_FORWARDED_FOR': '10.1.162.61',
    # 'HTTP_X_GATEWAY': 'wap.london.02.net',
