#coding:utf-8
import urllib.request
res = urllib.request.urlopen('https://www.python.org')
print(res.read().decode('utf-8'))
