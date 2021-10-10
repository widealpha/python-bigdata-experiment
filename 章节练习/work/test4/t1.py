def isAngle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True


def getArea(a, b, c):
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return S


if __name__ == "__main__":
    print("学号:2020328706   姓名:车明达")
    print("请输入三角形的第一条边：", end='')
    a = float(input())
    print("请输入三角形的第二条边：", end='')
    b = float(input())
    print("请输入三角形的第三条边：", end='')
    c = float(input())
    if isAngle(a, b, c):
        print("可以构成三角形")
        print("周长：%.6f" % (a + b + c))
        print("面积：%.6f" % (getArea(a, b, c)))
    else:
        print("不能构成三角形")
