def solve():
    for a in range(0, 100):
        for b in range(0, 100):
            for c in range(0, 100):
                if a + b + c == 78 and a == 2 * b + 4 and b == 3 * c - 2:
                    return a, b, c


if __name__ == '__main__':
    print("学号:2020328704   姓名:吴昀霏")
    a, b, c = solve()
    print("甲={}".format(a))
    print("乙={}".format(b))
    print("丙={}".format(c))
    print("{}+{}+{}={}".format(a, b, c, a + b + c))
