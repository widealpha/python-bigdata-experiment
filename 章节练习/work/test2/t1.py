if __name__ == '__main__':
    print("学号:2020328706   姓名:车明达")
    arr = []
    index = ['a', 'A', 'e', 'E', 'O', 'o', 'u', 'U', 'i', 'I']
    for i in range(1, 6):
        print("请输入第{}个英文单词：".format(i), end='')
        arr.append(input())
    print("输入的5个单词是{}".format(arr))
    print("首字母是元音的单词有")
    for s in arr:
        if s[0] in index:
            print(s)
