#coding:utf-8
import requests
file ={'file':open('test_1.py','rb')}
r = requests.post('http://httpbin.org/post',files = file)
print(r.text)
