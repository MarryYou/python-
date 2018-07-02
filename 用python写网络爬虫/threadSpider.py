#coding:utf-8
from threading import Thread
# from queue import queue
import time ,requests,json
from bs4 import BeautifulSoup

#起一个线程类
class DouBanSpider(Thread):
    def __init__(self,url,q):
        super(DouBanSpider,self).__init__()
        self.url = url
        self.q = q
        self.headers ={
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.proxies ={'http':'10.167.157.112:8118','https':'10.167.157.112:8118'}
    def run(self):
        self.parse_page()
    def send_request(self,url):
        i = 0
        while i <=3 :
            try:
                print('url:'+url)
                html = requests.get(url=url,proxies=self.proxies,headers=self.headers)
            except requests.ConnectionError as e:
                print('Error:'+e.args)
                i += 1
            else :
                return html
    def parse_page(self):
        res = self.send_request(self.url)
        html = BeautifulSoup(res.text,'lxml')
        content = html.find('body')
        self.q.put('content内容：'+content)
def main():
    # q = queue()
    with open('data.json') as f :
       urlList = json.load(f)
    print(urlList)
if __name__ == '__main__':
    main()
