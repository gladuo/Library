from __future__ import unicode_literals

from django.db import models
import jsonfield


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128, blank=True)
    isbn = models.IntegerField(unique=True, null=True, blank=True)
    douban_id = models.IntegerField(unique=True, null=True, blank=True)
    subtitle = models.CharField(max_length=128, blank=True)
    url = models.URLField()
    image = models.URLField(blank=True)
    images = jsonfield.JSONField(blank=True)  # a list
    author = jsonfield.JSONField(blank=True)  # a list
    author_intro = models.TextField(blank=True)
    translator = jsonfield.JSONField(blank=True)  # a list
    publisher = models.CharField(max_length=128, blank=True)
    pubdate = models.CharField(max_length=20, blank=True)
    binding = models.CharField(max_length=20, blank=True)
    pages = models.CharField(max_length=20, blank=True)
    price = models.CharField(max_length=20, blank=True)
    series = jsonfield.JSONField(blank=True)  # a list
    summary = models.TextField(blank=True)
    catalog = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    # behaviors = models.ManyToManyField(Behavior, blank=True)

    def __unicode__(self):
        return self.title


# class Behavior(models.Model):
#     done = models.ChoiceField(blank=True)
#     doing = jsonfield.JSONField(blank=True)
#     willing = jsonfield.JSONField(blank=True)
#
#     def __unicode__(self):
#         return self.
