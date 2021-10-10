import urllib.request
import _thread
import threading
from bs4 import BeautifulSoup

log = open("log.txt", mode='w', encoding='utf-8')
num = 0


class novel:
    chapter = ''
    content = ''


def get_chapter(index_url):
    urls = []
    try:
        response = urllib.request.urlopen(index_url, timeout=5)
        log.write("%s" % response.info())
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        for tag in soup.find_all(name='div', attrs={"id": "list"}):
            for herf in tag.find_all('a'):
                urls.append(index_url + herf['href'])
        log.write("%s" % urls)
    except Exception:
        log.write("获取章节目录出错，重试中")
        urls = get_chapter(index_url)
    finally:
        response.close()
    return urls


def get_content(url, c):
    content = ''
    try:
        response = urllib.request.urlopen(url, timeout=5)
        log.write("%s" % response.info())
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        title = soup.h1.string
        log.write(title)
        content = title + '\n'
        print(title)
        for text in soup.find_all(name='div', attrs={'id': 'content'}):
            content += text.text
            # print(content)
        c.content = content
        global num
        num += 1
    except Exception:
        get_content(url, c)
    finally:
        response.close()


def main():
    name = str(input("请输入小说的名字:"))
    url_start = str(input("输入导航页:"))
    log.write("name = {},url = {}".format(name, url_start))
    all_url = get_chapter(url_start)
    all_content = []
    i = 1
    for url in all_url:
        c = novel()
        c.chapter = i
        print("获取第%d章" % i)
        i += 1
        _thread.start_new_thread(get_content, (url, c))
        all_content.append(c)
    while True:
        x = input()
        if x == 'save':
            break
        print(num + 1, i, threading.active_count())
        if (num + 1 >= i) and (threading.active_count() == 1):
            break
    with open("{}.txt".format(name), mode='w+', encoding='utf-8') as file:
        for a in all_content:
            file.write("%s" % a.content)


main()
