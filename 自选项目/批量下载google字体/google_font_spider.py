"""爬取google差分字体"""
from os import listdir
from time import sleep

import requests
import re

from requests import RequestException, ReadTimeout


def main():
    url = 'https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Noto+Serif+JP:wght@400;700;900' \
          '&display=swap '
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
    }
    flag = True
    while flag:
        try:
            response = requests.get(url, headers=headers)
            urls_list = re.findall('https://.*\\.woff2', response.text)
            for url in urls_list[len(listdir('../spider/result/font/')):]:  # 从上一次爬取终止的地方继续爬取
                download_response = requests.get(url)
                with open('./result/font/' + url.split('/')[-1], 'wb') as file:
                    file.write(download_response.content)
            with open('result/font/style/font.css', 'w') as file:
                file.write(response.text.replace('https://fonts.gstatic.com/s', '../font'))
                flag = False
        except ReadTimeout:
            sleep(100)
        except RequestException:
            sleep(200)
    print('爬取完毕')
    return


if __name__ == '__main__':
    main()
