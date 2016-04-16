# coding=utf8

import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library.settings")

import django
django.setup()

from django.core.urlresolvers import reverse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from Books.models import Book, Tag

DIR = '/Users/ChaiDuo/Code/book_list'


def load_data(file_path='/Users/ChaiDuo/Code/Library/Library/编程.json'):
    with open(file_path, 'r') as f:
        for book_json in f.readlines():
            book = json.loads(book_json)
            print book["title"]
            for tag in book["tags"]:
                tag_obj, created = Tag.objects.get_or_create(name=tag["name"], slug=tag["title"])
                if created:
                    print 'tag', tag_obj
            try:
                book_data, created = Book.objects.get_or_create(isbn=book["isbn13"])
                if created:
                    try:
                        book_data.title = book["title"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.subtitle = book["subtitle"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.douban_id = book["id"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.author = book["author"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.translator = book["translator"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.publisher = book["publisher"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.image = book["image"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.images = book["images"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.pubdate = book["pubdate"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.url = '/book/' + str(book_data.id)
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.catalog = book["catalog"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.summary = book["summary"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.author_intro = book["author_intro"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.pages = book["pages"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.pubdate = book["pubdate"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.binding = book["binding"]
                    except (KeyError, ValueError):
                        pass
                    try:
                        book_data.pages = book["pages"]
                    except (KeyError, ValueError, UnicodeEncodeError):
                        pass
                    try:
                        book_data.price = book["price"]
                    except (KeyError, ValueError, UnicodeEncodeError):
                        pass
                    try:
                        book_data.series = book["series"]
                    except (KeyError, ValueError):
                        pass
                    print 'tags', book["tags"]
                    for tag in book["tags"]:
                        tag_obj = Tag.objects.get(name=tag["name"])
                        print tag_obj
                        book_data.tags.add(tag_obj)
                    book_data.save()
            except KeyError:
                pass


if __name__ == '__main__':
    for file in os.listdir(DIR):
        if os.path.splitext(file)[1] == '.json':
            load_data(os.path.join(DIR, file))
