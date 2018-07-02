# coding:utf-8
import requests
import time
from urllib.parse import urlencode
from pyquery import PyQuery as query
import os,re
base_url = 'https://www.toutiao.com/search_content/?'
proxies = {'http': '10.167.157.112:8118', 'https': '10.167.157.112:8118'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
    'x-requested-with': 'XMLHttpRequest'
}


def get_page(offest):
    params = {
        'offset': offest,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': 3,
        'from': 'gallery'
    }
    url = base_url + urlencode(params)
    try:
        res = requests.get(url, headers=headers, proxies=proxies)
        if res.status_code == 200:
            data = res.json()
            pic_list = []
            for _ in data['data']:
                for _item in _['image_list']:
                    pic_list.append(
                        {'title': _['title'], 'url': 'http:'+_item['url']})
            for item in pic_list:
                down_pic(item)
    except requests.ConnectionError as e:
        print('Error'+e.args)


def down_pic(object):
    header = {
        'Host': 'p1.pstatp.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    if not os.path.exists(object.get('title')):
        os.mkdir(object.get('title'))
    try:
        res = requests.get(object['url'], headers=header, proxies=proxies)
        if res.status_code == 200:   
            print()
            id = object['url'][-2:]
            file_path = '{0}/{1}.{2}'.format(object.get('title'), id, 'jpg')
            print(file_path)
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(res.content)
            else :
                print('Already Downloaded', file_path)
    except requests.ConnectionError as e:
        print('Error:'+e.args)


def main():
    for i in range(0, 140):
        get_page(offest=i * 20)
        time.sleep(1)
if __name__ == '__main__':
    main()
