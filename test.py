# coding=utf8

import requests
import json

URL = 'https://api.douban.com/v2/book/'


def fetch(url, book_id=24703171):
    # payload = {
    #     'id': str(book_id),
    # }
    r = requests.get(url+str(book_id))
    return r.status_code
    # book_content = json.loads(r.content)
    # for k, v in book_content.items():
    #     print k, v


if __name__ == '__main__':
    for i in range(0, int(1e9)):
        print i
        if fetch(URL, i) == 200:
            print 'OK !'
            break
