import urllib.request
from bs4 import BeautifulSoup

log = open("log.txt", mode='a+', encoding='utf-8')


def get_chapter(index_url):
    urls = []
    response = urllib.request.urlopen(index_url, timeout=5)
    log.write("%s" % response.info())
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all(name='div', attrs={"class": "article-list"}):
        for herf in tag.find_all('a'):
            urls.append(index_url + herf['href'])
    log.write("%s" % urls)
    return urls


def get_content(url):
    content = ''
    try:
        response = urllib.request.urlopen(url, timeout=5)
        log.write("%s" % response.info())
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        title = soup.h1.string
        log.write(title)
        # content = title + '\n'
        content = '\n'
        print(title)
        for text in soup.find_all(name='div', attrs={'id': 'content'}):
            content += text.text
            # print(content)
    except Exception:
        content = get_content(url)
    content = content.replace("傲轩小说网 www.axxsw.org 最快更新我想和你好好的最新章节！", "")
    return content


def main():
    name = str(input("请输入小说的名字:"))
    url_start = str(input("输入导航页:"))
    log.write("name = {},url = {}".format(name, url_start))
    all_url = get_chapter(url_start)
    i = 1
    for url in all_url:
        print("获取第%d章" % i)
        i += 1
        content = get_content(url)
        with open("%s.txt" % name, mode='a', encoding='utf-8') as file:
            file.write(content)
            file.close()


main()
