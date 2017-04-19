from django.db import models
from django.utils import timezone
from jsonfield.fields import JSONField
from tappil.links.models import Link


class Profile(models.Model):

    ip = models.GenericIPAddressField()
    device_family = models.TextField()
    device_os = models.TextField()
    device_version = models.TextField()
    uuid = models.TextField(unique=True, null=True, blank=True)
    user_agent = models.TextField()

    date_created = models.DateTimeField(default=timezone.now, null=True)
    link = models.ForeignKey(Link, related_name='profiles')
    meta_data = JSONField()
    installed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return '{} ({})'.format(self.ip, self.device_os)
