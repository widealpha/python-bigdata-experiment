import urllib.request
import time
import os
from bs4 import BeautifulSoup


def getpath(name):
    try:
        if len(name) == 0:
            name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        path = '/noval/' + name
        os.makedirs(path)
    except Exception:
        print("获取文件路径出错")
        return path
    return path


def gethtml(url):
    request = urllib.request
    a = request.urlopen(url)
    html = a.read()
    html = html.decode("utf-8")
    return html


def decode_html(soup):
    content = ''
    for text in soup.find_all(name='div', attrs={"class": "p"}):
        for p in text:
            if (len(p) == 0):
                break
            if p.string is None:
                continue
            content += "    "
            content += p.string
    return content


def get_next_url(soup, preUrl):
    nexUrl = None
    for tag in soup.find_all(name='li', attrs={"class": "next"}):
        nexUrl = "https://www.17k.com" + tag.a['href']
    return nexUrl


def get_noval_title(soup):
    print(soup.h1.string)
    return soup.h1.string


name = str(input("小说的名字:"))
noval_path = getpath(name)
start = int(input("开始的章节:"))
end = int(input("结束的章节:"))
url = str(input("输入小说起始网址:"))

html = gethtml(url)
soup = BeautifulSoup(html, 'lxml')

# decode_html(soup)
# get_next_url(soup, url)
# file_content = open(noval_path + '/content.html', mode="w+",\
#  encoding="utf-8")
# file_content.write(html)

i = start
while i <= end:
    print("获取第%d章中。。。" % i)
    name_chapter = get_noval_title(soup)
    # file_path = noval_path + '/第%d章_%s.txt' % (i, "ss")
    file_path = noval_path + '/' + name_chapter + '.txt'
    file = open(file_path, mode="w+", encoding="utf-8")
    file.write(name_chapter + '\n' + decode_html(soup))
    url = get_next_url(soup, url)
    html = gethtml(url)
    soup = BeautifulSoup(html, 'lxml')
    i += 1
