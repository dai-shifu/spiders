import os

import requests
from bs4 import BeautifulSoup


send_key = os.getenv('SEND_KEY')
send_key_bb = os.getenv('SEND_KEY_BB')
email = os.getenv('EMAIL')
passwd = os.getenv('PASSWD')

login_url = os.getenv('LOGIN_URL') or 'https://cv2.fun/auth/login'
target_urls = {
    'iOS': os.getenv('IOS_TUTORIAL_URL') or 'https://cv2.fun/user/tutorial?os=ios&client=shadowrocket',
    'Windows': os.getenv('WINDOWS_TUTORIAL_URL') or 'https://cv2.fun/user/tutorial?os=windows&client=cfw',
}

if not all((email, passwd, send_key, send_key_bb)):
    raise RuntimeError('缺少 EMAIL、PASSWD 或 Server酱 Key')

session = requests.Session()
login_data = {
    'email': email,
    'passwd': passwd,
    'code': '',
    'remember_me': 'on',
}
response = session.post(login_url, data=login_data, timeout=20)
response.raise_for_status()

clipboard_texts = {}
for platform, target_url in target_urls.items():
    target_page = session.get(target_url, timeout=20)
    target_page.raise_for_status()
    if target_page.url.startswith(login_url):
        raise RuntimeError('登录失败：教程页跳转到了登录页')
    soup = BeautifulSoup(target_page.text, 'html.parser')
    element = soup.find(attrs={'data-clipboard-text': True})
    clipboard_text = element.get('data-clipboard-text', '').strip() if element else ''
    if not clipboard_text:
        raise RuntimeError(f'{platform} 页面未找到有效的 data-clipboard-text')
    clipboard_texts[platform] = clipboard_text

message = f"## iOS\n{clipboard_texts['iOS']}\n\n## Windows\n{clipboard_texts['Windows']}"
failed_keys = []
for name, key in (('SEND_KEY', send_key), ('SEND_KEY_BB', send_key_bb)):
    try:
        response = requests.post(
            f'https://sctapi.ftqq.com/{key}.send',
            data={'title': 'vpn地址', 'desp': message},
            timeout=20,
        )
        response.raise_for_status()
    except requests.RequestException:
        failed_keys.append(name)

if failed_keys:
    raise RuntimeError(f"Server酱推送失败：{', '.join(failed_keys)}")
print('iOS 和 Windows 地址已推送')
