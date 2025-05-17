import requests
from bs4 import BeautifulSoup
import os
import json

proxies = {
    # 'http': 'http://127.0.0.1:7890',
    # 'https': 'http://127.0.0.1:7890',
}

# 使用环境变量读取敏感信息
send_key = os.getenv('SEND_KEY')
send_key_bb = os.getenv('SEND_KEY_BB')
email = os.getenv('EMAIL')
passwd = os.getenv('PASSWD')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'Referer': 'https://cv2.info/auth/login',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

# 模拟登录的URL
login_url = 'https://cv2.info/auth/login'

target_url = 'https://cv2.info/user/tutorial?os=windows&client=cfw'

session = requests.Session()

login_data = {
    'email': email,
    'passwd': passwd,
    'code': '',
    'remember_me': 'on',
}

response = session.post(login_url, data=login_data, proxies=proxies, allow_redirects=True)

if response.status_code == 200:
    if 'info/user' not in response.url:
        # 访问目标页面
        target_page = session.get(target_url, proxies=proxies)

        soup = BeautifulSoup(target_page.text, 'html.parser')

        # 查找目标
        element = soup.find(attrs={"data-clipboard-text": True})
        if element:
            clipboard_text = element.get('data-clipboard-text')
            print(clipboard_text)
            webhook_url = f'https://sctapi.ftqq.com/{send_key}.send?title=vpn地址&desp={clipboard_text}'
            webhook_url_bb = f'https://sctapi.ftqq.com/{send_key_bb}.send?title=vpn地址&desp={clipboard_text}'

            try:
                response = requests.post(webhook_url)
                response_bb = requests.post(webhook_url_bb)

            except Exception as e:
                print('发送通知失败')

        else:
            print('未找到目标')
    else:
        print('登录失败', response.url, response.json())
else:
    print('登录失败')
