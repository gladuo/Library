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
    title = models.CharField(max_length=128)
    isbn13 = models.IntegerField(unique=True, null=True)
    douban_id = models.IntegerField(unique=True)
    subtitle = models.CharField(max_length=128)
    url = models.URLField()
    image = models.URLField()
    author = jsonfield.JSONField()  # a list
    author_intro = models.TextField()
    translator = jsonfield.JSONField()  # a list
    publisher = models.CharField(max_length=128)
    pubdate = models.CharField(max_length=20)
    tags = jsonfield.JSONField()  # a list
    binding = models.CharField(max_length=20)
    pages = models.IntegerField()
    price = models.CharField(max_length=20)
    series = jsonfield.JSONField()  # a list
    summary = models.TextField()
    catalog = models.TextField()
    tag_category = models.ManyToManyField(Tag)

    def save(self, *args, **kwargs):
        super(Book, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title






