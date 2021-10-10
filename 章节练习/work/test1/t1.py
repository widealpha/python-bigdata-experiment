if __name__ == '__main__':
    print("学号:2020328704   姓名:吴昀霏")
    print("请输入1-9整数：", end='')
    a = int(input())
    b = a
    print("请输入相加的个数（大于1的正整数：）", end='')
    c = int(input())
    ans = 0
    for i in range(c):
        ans += a
        a = a * 10 + b
    print("{}+...+{}的和是： {}".format(b, a, ans))
