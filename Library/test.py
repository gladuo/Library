# coding=utf8

import json

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library.settings")

import django
django.setup()

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from Books.models import Book


def load_data():
    with open('', 'r') as f:
        for book_json in f.readlines():
            print book_json
            book = json.loads(book_json)
            print book["title"]
            try:
                book_data = Book()
                book_data.title = book["title"]
                book_data.subtitle = book["subtitle"]
                book_data.isbn = book["isbn13"]
                book_data.douban_id = book["id"]
                book_data.author = book["author"]
                book_data.translator = book["translator"]
                book_data.publisher = book["publisher"]
                book_data.image = book["image"]
                book_data.pubdate = book["pubdate"]
                book_data.url = book["url"]
                book_data.catalog = book["catalog"]
                book_data.summary = book["summary"]
                book_data.author_intro = book["author_intro"]
                book_data.pages = book["pages"]
                book_data.pubdate = book["pubdate"]
                book_data.tags = book["tags"]
                book_data.binding = book["binding"]
                book_data.price = book["price"]
                book_data.series = book["series"]
            except ValueError:
                pass
            except KeyError:
                pass

            book_data.save()


if __name__ == '__main__':
    load_data()
