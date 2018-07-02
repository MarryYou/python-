#coding:utf-8
import requests,time
import json
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def get_one_page(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        content = BeautifulSoup(res.text,'lxml')
        imgs  = content.find_all('img', class_="board-img")
        numbers = content.find_all('i', class_="board-index")
        titles = content.find_all('div', class_="movie-item-info")
        data = []
        for index in range(len(imgs)):
            number = numbers[index].text
            board_img = imgs[index].attrs['data-src']
            name = titles[index].contents[1].text
            anthor = titles[index].contents[3].text
            time = titles[index].contents[5].text
            data.append({'number':number,'board_img':board_img,'name':name,'anthor':anthor,'time':time})
        return data
    return None
def main(offest):
    url = 'http://maoyan.com/board/4?offest?'+str(offest)
    html = get_one_page(url)
    return html
if __name__ == '__main__':
    jsonData = []
    for i in range(10):
        Data = main(offest=i*10)
        jsonData += Data
        time.sleep(1)
    with open('data.json','w+',encoding='utf-8') as f:
        json.dump(jsonData,f)
    print('爬取完成')
