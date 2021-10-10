import os
import json

if __name__ == '__main__':
    os.system('scrapy crawl sdu_news -s LOG_FILE=spider.log -O news.json')
    while True:
        keyword = input('请输入想要搜索的关键字(直接回车退出):\n')
        if len(keyword) == 0:
            break
        try:
            with open('news.json') as news_file:
                new_infos = []
                news_list = json.load(news_file)
                for new in news_list:
                    if keyword in new['keywords']:
                        new_infos.append(new)
                print('全文搜索中包含有关键字"%s"的共有%d篇文章:' % (keyword, len(new_infos)))
                for index, news_info in enumerate(new_infos):
                    print(str(index + 1) + '.')
                    print('     标题:%s' % news_info['title'])
                    print('     发布日期:%s' % news_info['date'])
                    print('     新闻链接:%s' % news_info['link'])
                    print('========================================================================')
                confirm = input('是否查看详情(y/n):')
                if confirm.startswith('y'):
                    while True:
                        try:
                            new_id = int(input('请输入想要查看的编号(按q退出):'))
                            print('     标题:%s' % new_infos[new_id - 1]['title'])
                            print('     发布日期:%s' % new_infos[new_id - 1]['date'])
                            print('     内容:%s' % new_infos[new_id - 1]['content'])
                            print('     新闻链接:%s' % new_infos[new_id - 1]['link'])
                            print('===================================================================')
                        except ValueError:
                            break
                        except IndexError:
                            print('id不存在,请重新输入')
                            continue
        except IOError:
            print('error in file')
            exit(-1)
        except json.decoder.JSONDecodeError:
            print('error in json')
            exit(-1)

