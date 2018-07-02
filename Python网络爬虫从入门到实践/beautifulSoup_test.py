#coding:utf-8
import requests,time
from bs4 import BeautifulSoup
import pymongo,time,re
headers = {
    'referer': 'https://nanjing.anjuke.com/sale/?from=navigation',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url = 'https://nanjing.anjuke.com/sale/p'
proxies = {'http': '10.167.157.112:8118', 'https': '10.167.157.112:8118'}
def downloader(url,headers,proxies):
    try:
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client.anjuke
        collection = db.hourse_data
        res = requests.get(url=url,headers=headers,proxies=proxies)
        if res.status_code == 200 :
            html = BeautifulSoup(res.text, 'lxml')
            div = html.find_all('div', class_='sale-left')
            hourse_list = BeautifulSoup(str(div), 'lxml').find_all(
                'li', class_='list-item')
            img_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('img')
            title_list = BeautifulSoup(str(hourse_list), 'lxml').find_all(
                'a', class_='houseListTitle')
            details_list = BeautifulSoup(str(hourse_list), 'lxml').find_all(
                'div', class_='details-item')
            address_list = BeautifulSoup(str(hourse_list), 'lxml').find_all(
                'span', class_='comm-address')
            prices_list = BeautifulSoup(str(hourse_list), 'lxml').find_all(
                'div', class_='pro-price')
            colection_data = []
            for item in range(0, len(hourse_list)):
                colection_data.append({
                    'img_src': img_list[item]['src'],
                    'title': re.sub(r'\/W.', '', title_list[item].text),
                    'details': re.sub('', '|', details_list[item].text),
                    'address': address_list[item].text,
                    'priceAll': prices_list[item].contents[1].text,
                    'price': prices_list[item].contents[2].text
                })
            collection.insert_many(colection_data)
            print('success insert data')
    except requests.ConnectionError as e:
        print('Error:'+e.args)
    
def main():
    for _ in range(1,10):
        downloader(url+str(_), headers, proxies)
        time.sleep(1)
    # res =requests.get(url=url,proxies=proxies,headers=headers)
    # html = BeautifulSoup(res.text,'lxml')
    # div = html.find_all('div', class_='sale-left')
    # hourse_list = BeautifulSoup(str(div), 'lxml').find_all( 'li', class_='list-item')
    # img_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('img')
    # title_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('a', class_='houseListTitle')
    # details_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('div', class_='details-item')
    # address_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('span', class_='comm-address')
    # prices_list = BeautifulSoup(str(hourse_list), 'lxml').find_all('div', class_='pro-price')
    # print(address_list[0].contents)
    # colection_data =[]
    # for item in range(0, len(hourse_list)):
    #     colection_data.append({
    #         'img_src': img_list[item]['src'],
    #         'title': re.sub(r'\/W.', '', title_list[item].text),
    #         'details': details_list[item].text,
    #         'address': address_list[item].text,
    #         'priceAll': prices_list[item].contents[1].text,
    #         'price': prices_list[item].contents[2].text
    #     })
    
    # print(colection_data[0])
if __name__ == '__main__':
    main()
