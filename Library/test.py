# coding=utf8

import requests
# import json

# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Library.settings")
#
# import django
# django.setup()
#
# from Books.models import Book

URL = 'https://api.douban.com/v2/book/'


def fetch(url=URL, book_id=24703171):
    r = requests.get(url+str(book_id))
    print r.text

    # for k, v in p.items():
    #     print repr(k), repr(v)
    # return r.status_code
    # book_content = json.loads(r.content)
    # for k, v in book_content.items():
    #     print k, v




if __name__ == '__main__':
    fetch()
