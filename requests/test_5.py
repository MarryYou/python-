# coding:utf-8
import requests
from pyquery import PyQuery as query
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
def main():
    html = requests.get(url,headers=headers).text
    doc  = query(html)
    items = doc('.explore-tab .feed-item').items()
    for item in items:
        question = item.find('h2').text()
        anthor = item.find('.author-link-line').text()
        answer = query(item.find('.content').html()).text()
        with open('explore.txt','a',encoding='utf-8') as f:
            f.write('\n'.join([question,anthor,answer]))
            f.write('\n'+'='* 50 +'\n')


if __name__ == '__main__':
    main()
