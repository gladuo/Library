# coding=utf-8

import requests
import json
import time

URL = 'https://api.douban.com/v2/book/isbn/'


def download():
    with open('book.txt', 'a+') as f:
        for i in range(13600, int(1e5), 10):
            r = requests.get(URL+'9787'+'%09d' %i)
            while r.status_code == 403:
                print '--- Sleeping now ! ---'
                time.sleep(60)
                r = requests.get(URL+'9787'+'%09d' %i)
            cont = json.loads(r.text)
            print cont
            try:
                msg = cont['msg']
                print 'Isbn '+'9787'+'%09d' %i+' is empty !'
                continue
            except KeyError:
                f.write(r.text.encode('utf-8')+'\n')
                print 'Book %s is downloaded !' %cont['title'].encode('utf-8')
                print 'Isbn '+'9787'+'%09d' %i


if __name__ == '__main__':
    download()
