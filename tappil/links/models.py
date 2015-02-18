from django.db import models
from tappil.referrers.models import Referrer


class Link(models.Model):

    url = models.URLField()
    referrer = models.ForeignKey(Referrer, related_name='links')
    deep_link = models.TextField()