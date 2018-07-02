#coding:utf-8
import requests
from selenium import webdriver 
from bs4 import BeautifulSoup
post_url = 'http://arxiv-sanity.com/'
headers={
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
}
proxies = {'http': '10.167.196.133:8080', 'https': '10.167.196.133:8080'}
driver = webdriver.Chrome()

res = requests.get(url=post_url, proxies=proxies, headers=headers)
html= BeautifulSoup(res.text,'lxml')

with open('data.html','w') as f:
    f.write(res.text)