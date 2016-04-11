from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(default=20)
    SEX = (
        ('boy', 'male'),
        ('girl', 'female'),
    )
    gender = models.CharField(max_length=1, choices=SEX)
    university = models.CharField(max_length=128)
    description = models.TextField()

    def __unicode__(self):
        return self.username
