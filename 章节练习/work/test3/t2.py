if __name__ == '__main__':
    lists = [
        {'id': 1, 'name': '糖糖', '爱好': '美食'},
        {'id': 2, 'name': '理理', '爱好': '音乐'},
        {'id': 3, 'name': '南南', '爱好': '电竞'},
        {'id': 4, 'name': '苏苏', '爱好': '美妆'},
    ]
    print('欢迎使用学生查询系统')
    print('学号格式：*(*的取值为正整数)')
    while True:
        id = int(input('请输入您想查询的学号:'))
        for m in lists:
            if m['id'] == id:
                print('您查询的结果为')
                print('姓名： ' + m['name'])
                print('爱好： ' + m['爱好'])
        a = input('您想继续查询吗? Y/N')
        if a in ['Y', 'y']:
            continue
        else:
            break
    print('谢谢使用！再见！')
