def mod_mul(x, y, c):
    return x ** y % c


# python不限整数运算精度
if __name__ == '__main__':
    print(mod_mul(123456789, 12, 12345678))
