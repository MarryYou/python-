#coding:utf-8
import requests
from urllib.parse import urlencode
import json
from bs4 import BeautifulSoup
from pyquery import PyQuery as query
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers ={
    'Host':'m.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
proxies = {'http':'10.167.157.112:8118','https':'10.167.157.112:8118'}

def get_page(page):
    params = {
        'type':'uid',
        'value': '2145291155',
        'containerid': '1076032145291155',
        'page':page
    }
    url = base_url + urlencode(params)
    try:
        res = requests.get(url,headers=headers,proxies=proxies,verify=False)
        if res.status_code == 200:
            with open('data.json','w') as f :
                json.dump(res.json(),f)
    except requests.ConnectionError as e:
        print(e.args)
# def parse_page(json):
#     if json:
        
def main():
    get_page(1)

if __name__ == '__main__':
    main()
