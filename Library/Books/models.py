from __future__ import unicode_literals

from django.db import models
import jsonfield


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.CharField(max_length=20)
    # Todo: add books

    def __unicode__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=128, blank=True)
    isbn = models.IntegerField(unique=True, null=True, blank=True)  # Todo: modify
    douban_id = models.IntegerField(unique=True, null=True, blank=True)  # Todo: modify
    subtitle = models.CharField(max_length=128, blank=True)
    url = models.URLField()
    image = models.URLField(blank=True)
    author = jsonfield.JSONField(blank=True)  # a list
    author_intro = models.TextField(blank=True)
    translator = jsonfield.JSONField(blank=True)  # a list
    publisher = models.CharField(max_length=128, blank=True)
    pubdate = models.CharField(max_length=20, blank=True)
    tags = jsonfield.JSONField(blank=True)  # a list
    binding = models.CharField(max_length=20, blank=True)
    pages = models.IntegerField(blank=True, null=True)
    price = models.CharField(max_length=20, blank=True)
    series = jsonfield.JSONField(blank=True)  # a list
    summary = models.TextField(blank=True)
    catalog = models.TextField(blank=True)
    tag_category = models.ManyToManyField(Tag, blank=True)

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title






