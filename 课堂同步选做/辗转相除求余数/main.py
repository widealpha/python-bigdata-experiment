def gcf(x, y, hcf):
    smaller = x if x > y else y
    for i in range(1, smaller + 1):
        hcf = i if (x % i == 0) and (y % i == 0) else hcf
    return hcf


if __name__ == '__main__':
    x = int(input('x'))
    y = int(input('y'))
    hcf = 1
    print(gcf(x, y, hcf))
