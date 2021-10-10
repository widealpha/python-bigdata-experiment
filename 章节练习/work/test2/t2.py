if __name__ == '__main__':
    print("学号:2020328704   姓名:吴昀霏")
    str1 = input('请输入第一个字符串:')
    str2 = input('请输入第二个字符串:')

    for c in str2:
        str1 = str1.replace(c, '')
    print(str1)
