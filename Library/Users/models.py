from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age = models.IntegerField(default=20)
    SEX = (
        ('boy', 'male'),
        ('girl', 'female'),
    )
    gender = models.CharField(max_length=1, choices=SEX)
    group = models.CharField(max_length=20)
