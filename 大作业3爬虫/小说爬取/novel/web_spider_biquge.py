import urllib.request
import time
import os
from bs4 import BeautifulSoup
from io import BytesIO
import gzip


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
    req = urllib.request.Request(url)
    # req.add_header('Connection', 'keep-alive')
    # req.add_header('Cache-Control', 'max-age=0')
    # req.add_header('Upgrade-Insecure-Request', '1')
    # req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)\
    #      AppleWebKit/537.36 (KHTML, like Gecko)\
    #           Chrome/58.0.3029.110 Safari/537.36')
    # req.add_header('Accept', \
    # 'text/html,application/xhtml+xml,application/xml;\
    #     q=0.9,image/webp,*/*;q=0.8')
    req.add_header('Accept-Encoding', 'gzip, deflate, sdch, br')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6')
    response = urllib.request.urlopen(req)
    print(response.info())
    try:
        buf = BytesIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        f_html = f.read()
        # f_html = f_html.decode('utf-8')
    except Exception as e:
        print(e)
    # print(f_html)
    return f_html


def decode_html(soup):
    content = ''
    for text in soup.find_all(name='div', attrs={"id": "content"}):
        content += text.text
        # print(text.text)
        # for p in text:
        #     print(p.string)
        #     if (len(p) == 0):
        #         break
        #     if p.string is None:
        #         continue
        #     content += "    "
        #     content += p.string
    return content


def get_next_url(soup, preUrl):
    nexUrl = None
    for a in soup.select('a'):
        # print(a.string)
        if a.string == '下一章':
            nexUrl = a['href']
            break
    print(nexUrl)
    return nexUrl


def get_noval_title(soup):
    print(soup.h1.string)
    return soup.h1.string


name = str(input("小说的名字:"))
noval_path = getpath(name)
start = int(input("开始的章节:"))
end = int(input("结束的章节:"))

# start = 1
# end = 100

url = str(input("输入小说起始网址:"))

html = gethtml(url)
soup = BeautifulSoup(html, 'lxml')
# decode_html(soup)
# get_next_url(soup, url)
# file_content = open(noval_path + '/content.txt', mode="w+", encoding="utf-8")
# file_content.write(html)

i = start
while i <= end:
    print("获取第%d章中。。。" % i)
    name_chapter = get_noval_title(soup)
    # file_path = noval_path + '/第%d章_%s.txt' % (i, "ss")
    file_path = noval_path + '/' + name_chapter + '.txt'
    file = open(file_path, mode="w+", encoding="utf-8")
    file.write(name_chapter + '\n' + decode_html(soup))
    file.close
    url = get_next_url(soup, url)
    html = gethtml(url)
    soup = BeautifulSoup(html, 'lxml')
    i += 1
