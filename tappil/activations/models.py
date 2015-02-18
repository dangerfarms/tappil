from django.db import models
from tappil.links.models import Link


class Activation(models.Model):

    link = models.ForeignKey(Link)
    ip_address = models.IPAddressField()
    device = models.TextField()