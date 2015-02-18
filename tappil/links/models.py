from django.db import models
from tappil.referrers.models import Referrer


class Link(models.Model):

    code = models.TextField()
    referrer = models.ForeignKey(Referrer, related_name='links')
    deep_link = models.TextField()


