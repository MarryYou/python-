#coding:utf-8
import requests
import re
headers ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
title   = re.findall(pattern,r.text)
print(title)
print(r.cookies)