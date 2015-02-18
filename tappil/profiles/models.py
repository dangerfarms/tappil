from django.db import models
from jsonfield.fields import JSONField


class Profile(models.Model):

    profile_id = models.TextField(unique=True)
    data = JSONField()