# qnrepo

import requests
import time

# Proxy listesini almak için fonksiyon
def get_proxy_list(url):
    response = requests.get(url)
    return response.text.strip().splitlines()

# Proxy listesini formatlamak için fonksiyon
def format_proxy_list(proxy_list):
    formatted_list = []
    for proxy in proxy_list:
        if ':' in proxy:
            parts = proxy.split(':')
            formatted_proxy = f"socks5://{parts[0]}:{parts[1]}"
            formatted_list.append(formatted_proxy)
    return formatted_list

# Proxy'nin çalışıp çalışmadığını kontrol etmek için fonksiyon
def check_proxy(proxy):
    try:
        response = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
        print(response.text)
        return response.status_code == 200
    except:
        return False

# Proxy listesini alacağınız URL
url="https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt"

# Proxy listesini alıp formatlayın
proxies = get_proxy_list(url)
formatted_proxies = format_proxy_list(proxies)
# Çalışan proxy'leri bulun
working_proxies = [proxy for proxy in formatted_proxies if check_proxy(proxy)]

def convert_formatprox(working_proxies):
    new_format_list=[]
    for proxy in working_proxies:
        if proxy.startswith("socks5://"):
            stripped_proxy=proxy.replace("socks5://","")
            ip,port=stripped_proxy.split(":")
            new_format=f'socks5 {ip} {port}'
            new_format_list.append(new_format)
    return new_format_list    

newformat=convert_formatprox(working_proxies)

# Proxychains.conf dosyasını güncelleyin
with open('/etc/proxychains.conf', 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
        if '[ProxyList]' in line:
            break
        file.write(line)
    file.write('[ProxyList]\n')
    for proxy in newformat:
        file.write(f"{proxy}\n")
    file.truncate()  # Dosyanın geri kalanını temizleyin

with open("socks5.txt", "w+") as file:
    for proxy in newformat:
        file.write(f"{proxy}\n")
    file.close()
print(f"Çalışan proxy bilgileri proxychains.conf dosyasına eklendi: {working_proxies}")