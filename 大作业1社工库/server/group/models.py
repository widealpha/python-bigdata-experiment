from django.db import models
import pymssql


# Create your models here.

def get_relation(qun_num=None, qq_num=None):
    connect = pymssql.connect(r'DESKTOP-DPESRRO\MSSQLSERVER01', 'SA', '@Abc123456', 'qqqun',
                              charset='cp936')  # 服务器名,账户,密码,数据库名

    nodes_id_list = []
    nodes = []
    links = []
    categories = [{
        "name": "个人"
    }, {
        "name": "QQ群"
    }]
    cursor = connect.cursor()  # 创建一个游标对象,python里的sql语句都要通过cursor来执行
    if qq_num:
        qq_num = int(qq_num)
        nodes_id_list.append('qq' + str(qq_num))
    elif qun_num:
        qun_num = int(qun_num)
        nodes_id_list.append('qun' + str(qun_num))
    enrich(cursor, nodes_id_list, links, nodes)
    enrich(cursor, nodes_id_list, links, nodes)
    cursor.close()  # 关闭游标
    connect.close()  # 关闭连接
    return {'categories': categories, 'links': links, 'nodes': nodes}


def enrich(cursor, node_list, links, nodes):
    node_list_back = node_list.copy()
    for node_id in node_list_back:
        try:
            if node_id.startswith('qq'):
                cursor.execute("select * from qqq where QQNum = " + str(node_id.split('qq')[-1]))
            elif node_id.startswith('qun'):
                cursor.execute("select * from qqq where QunNum = " + str(node_id.split('qun')[-1]))
            rows = cursor.fetchall()
            for row in rows:
                qq_id = str('qq' + str(row[1]))
                qun_id = str('qun' + str(row[6]))
                if {'source': qq_id, 'target': qun_id} not in links:
                    links.append({'source': qq_id, 'target': qun_id})
                if (len(node_list) == 1) & (len(nodes) == 0):
                    if node_list[0].startswith('qq'):
                        nodes.append({'id': qq_id, 'name': row[2], 'symbolSize': 20, 'category': 0})
                    elif node_list[0].startswith('qun'):
                        nodes.append({'id': qun_id, 'name': qun_id, 'symbolSize': 40, 'category': 1})
                if qq_id not in node_list:
                    node_list.append(qq_id)
                    nodes.append({'id': qq_id, 'name': row[2], 'symbolSize': 20, 'category': 0})
                if qun_id not in node_list:
                    try:
                        cursor.execute("select * from list where QunNum = " + qun_id[3:])
                        r = cursor.fetchone()
                        node_list.append(qun_id)
                        nodes.append({'id': qun_id, 'name': r[3], 'symbolSize': 40, 'category': 1})
                    except pymssql.StandardError as e:
                        node_list.append(qun_id)
                        nodes.append({'id': qun_id, 'name': qun_id, 'symbolSize': 40, 'category': 1})
        except pymssql.StandardError as e:
            print(e)
