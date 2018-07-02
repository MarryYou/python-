#coding:utf-8

import requests,re,os
from bs4 import BeautifulSoup
from PIL import Image
def get_si_code():
    index_url = 'http://www.santostang.com/wp-login.php?action=register'
    index_page = session.get(index_url, headers=headers, proxies=proxies)
    html = index_page.text
    si_code_input = BeautifulSoup(html,'lxml')
    si_code = si_code_input.find('input', id='si_code_reg')
    print()
    return si_code.attrs['value']
def get_captcha(si_code):
    captcha_url = 'http://www.santostang.com/wp-content/plugins/si-captcha-for-wordpress/captcha/securimage_show.php?si_sm_captcha=1&si_form_id=reg&prefix='+si_code
    res = session.get(captcha_url, headers=headers, proxies=proxies)
    with open('captcha.jpg','wb') as f:
        f.write(res.content)
        f.close()
    try:
        im = Image.open('captcha.jpg')
        im.show()
        im.close()
    except :
        print('请到%s目录下找到capatcha.jpg说多那个输入'%os.path.abspath('captcha.jpg'))
    captcha = input('please input the captcha \n>')
    return captcha
def register(account,email,si_code):
    post_url = 'http://www.santostang.com/wp-login.php?action=register'
    postdata ={
        'user_login':account,
        'user-email':email,
        'si_code_reg':si_code,
        'redirect_to':'',
    }
    postdata['captcha'] = get_captcha(si_code)
    register_page = session.post(post_url, data=postdata, headers=headers, proxies=proxies)
    print(register_page.status_code)
if __name__=='__main__':
    session = requests.session()
    headers = {
        'Referer': 'http://www.santostang.com/wp-login.php',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Host': 'www.santostang.com',
        'Origin': 'http://www.santostang.com'
    }
    proxies = {'http': '10.167.196.133:8080', 'https': '10.167.196.133:8080'}
    si_code = get_si_code()
    account = '14752268465'
    email='456123799@qq.com'
    register(account,email,si_code)
