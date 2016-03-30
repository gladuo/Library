from __future__ import unicode_literals

from django.db import models
import jsonfield


class Book(models.Model):
    douban_id = models.IntegerField(unique=True,)
    isbn13 = models.IntegerField(unique=True,)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    url = models.URLField()
    image = models.URLField()
    author = jsonfield.JSONField()  # a list
    translator = jsonfield.JSONField()  # a list
    publisher = models.CharField(max_length=128)
    pubdate = models.DateField()
    tags = jsonfield.JSONField()  # a list
    binding = models.CharField(max_length=128)
    price = models.FloatField()
    series = jsonfield.JSONField()  # a list
    pages = models.IntegerField()
    author_intro = models.TextField()
    summary = models.TextField()
    catalog = models.TextField()

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name



