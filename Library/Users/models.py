# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import jsonfield


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    age = models.IntegerField(default=20)
    SEX = (
        ('male', 'boy'),
        ('female', 'girl'),
    )
    gender = models.CharField(max_length=6, choices=SEX, default='male')
    university = models.CharField(max_length=128, blank=True)
    description = models.TextField(max_length=128, blank=True)
    history = jsonfield.JSONField(blank=True, default=[u'20345'])
    favorite_tag = jsonfield.JSONField(blank=True, default={})

    def __unicode__(self):
        return self.user.username
