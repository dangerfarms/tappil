from django.db import models
from jsonfield.fields import JSONField


class Profile(models.Model):

    ip = models.IPAddressField()

    device_family = models.TextField() # iPhone
    device_os = models.TextField() # iOS
    device_version = models.TextField() # 8.0.2

    meta_data = JSONField()

    # port REMOTE_PORT
    # language_  'HTTP_ACCEPT_LANGUAGE': 'en-GB,en;q=0.8,en-US;q=0.6,hu;q=0.4',
    # 'HTTP_X_FORWARDED_FOR': '10.1.162.61',
    # 'HTTP_X_GATEWAY': 'wap.london.02.net',
