import urllib.request
from bs4 import BeautifulSoup

log = open("log.txt", mode='a+', encoding='utf-8')


def get_chapter(index_url):
    urls = []
    get = True
    response = None
    print("获取导航页中。。。")
    log.write("获取导航页")
    while get:
        try:
            response = urllib.request.urlopen(index_url, timeout=5)
            get = False
        except Exception as e:
            print(e)
            log.write("获取导航页失败，准备再次尝试,错误%s" % e)
            get = True

    log.write("导航页获取完毕，状态：")
    log.write("%s" % response.info())
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    for tag in soup.find_all(name='div', attrs={"class": "ml_list"}):
        for herf in tag.find_all('a'):
            try:
                urls.append("https://www.djyzx.com" + herf['href'])
            except Exception:
                pass
    log.write("%s" % urls)
    log.write("共%d章" % len(urls))
    return urls


def get_content(url):
    content = ''
    try:
        response = urllib.request.urlopen(url, timeout=5)
        log.write("%s" % response.info())
        html = response.read()
        soup = BeautifulSoup(html, 'lxml')
        title = soup.h3.string
        log.write(title)
        content = '\n' + title + '\n'
        print(title)
        for text in soup.find_all(name='p', attrs={'id': 'articlecontent'}):
            content += text.text
            # print(content)
    except Exception:
        print("获取内容超时")
        content = get_content(url)
    return content


def main():
    name = str(input("请输入小说的名字:"))
    url_start = str(input("输入导航页:"))
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
