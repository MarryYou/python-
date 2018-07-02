#coding:utf-8
import requests
res = requests.get('https://www.baidu.com')
print(type(res))
print(res.status_code)
print(res.text)
print(type(res.text))
print(res.cookies)