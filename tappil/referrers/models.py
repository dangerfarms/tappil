from django.db import models


class Referrer(models.Model):

    name = models.TextField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name