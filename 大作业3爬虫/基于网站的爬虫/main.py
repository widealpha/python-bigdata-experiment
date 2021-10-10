import requests
import re
import os

from requests import RequestException

base_url = ''


def main():
    global base_url
    web_url, level = init_url_level()
    base_url = web_url
    if 'http://' in base_url:
        base_url = base_url.split('http://')[-1]
    elif 'https://' in base_url:
        base_url = base_url.split('https://')[-1]
    spider([web_url], 0, level)


def init_url_level():
    try:
        web_url = input('请输入想要爬取网站的根目录:')
        level = int(input('请输入想要爬取的层数(默认为3):'))
        if level <= 0:
            level = 3
        return web_url, level
    except ValueError:
        print('输入格式有误,请检查输入数据\n')
        print('层数是指爬取的网页的深度,必须为整数\n')
        return 3


def spider(url_list, level, max_level):
    if not os.path.exists('./result/' + base_url):
        os.makedirs('./result/' + base_url)
    if level >= max_level:
        return
    urls = []
    for url in url_list:
        try:
            content = response_content_get(url)
            if len(content) > 0:
                filename = url
                if url == base_url:
                    filename = 'index.html'
                elif '/' in filename:
                    filename = filename.split('/')[-1]
                file = open('./result/' + base_url + '/' + filename, mode='w+', encoding='utf-8')
                file.write(content)
            print(content)
            link_list = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", process_content(content))
            urls = link_list
        except IOError as e:
            print(e)
            continue
    if len(urls) > 0:
        spider(urls, level + 1, max_level)
    else:
        print('在爬取第' + str(level) + '层时,爬取工作结束')
        return


def response_content_get(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    try:
        # 如果根网页没有指定协议，就指定为http协议
        if ('://' not in url) & (len(url) > 0) & (url == base_url):
            url = 'http://' + url
        # 如果链接协议不是http/https被认为是不可抓取的链接,尝试添加base_url后进行捕捉
        if ('http' not in url) & ('https' not in url):
            url = 'http://' + base_url + url
        response = requests.get(url, headers=headers)
        return response.text
    except RequestException as e:
        print(str(e))
        return ''


def process_content(content):
    return content.replace('https%3A//', 'https://').replace('http%3A//', 'http://') \
        .replace('http%3A%2F%2F', 'http://').replace('https%3A%2F%2F', 'https://')


if __name__ == '__main__':
    main()
