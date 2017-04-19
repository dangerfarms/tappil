from django.db import models


class Device(models.Model):

    uuid = models.TextField(null=True)
    family = models.TextField(null=True)
    os = models.TextField(null=True)
    version = models.TextField(null=True)

    def __str__(self):
        return '{} {} {}'.format(self.family, self.os, self.version)
