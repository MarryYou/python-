#coding:utf-8
import requests,time,json
from bs4 import BeautifulSoup

proxies = {'http': '10.167.157.112:8118', 'https': '10.167.157.112:8118'}
def download_url():
    data = []
    try:
        res = requests.get(url='https://www.alexa.com/topsites',proxies=proxies)
        html = BeautifulSoup(res.text,'lxml')
        lists = html.find_all('div', class_='tr site-listing')
        divs = BeautifulSoup(str(lists), 'lxml').find_all('div', class_='td DescriptionCell')
        tag_p = BeautifulSoup(str(divs), 'lxml').find_all('p')
        links = BeautifulSoup(str(tag_p), 'lxml').find_all('a')
        for link in links:
            str_split = link['href'].split('/')
            data.append({'title':link.text,'url':'www.'+str_split[2]})
        with open('data.json','w+') as f:
            json.dump({'data': data}, f)
    except requests.ConnectionError as e:
        print('Error:'+e.args)

def main():
    download_url()

if __name__ == '__main__':
    main()
