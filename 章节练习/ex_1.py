import random


def main():
    test_divide()
    test_map()
    test_prime()
    test_monty()
    return


def test_divide():
    """虽然有更简单的但是这儿是题目要求"""
    x = int(input('请输入数字'))
    print(str(x // 100))


def test_prime():
    """素数筛子"""
    prime_array = [True] * 101
    prime_array[0] = False
    prime_array[1] = False

    prime = []

    i = 2
    while i <= 100:
        if prime_array[i]:
            prime.append(i)
            if i * i <= 100:
                j = i * i
                while j <= 100:
                    prime_array[j] = False
                    j += i
        i += 1


def test_map():
    """第二章作业2"""
    t_map = {'a': 1, 'b': 2, 'c': 3, 'd': 1}
    x = input("请输入键")
    if t_map[x] is None:
        print('没有该键')
    else:
        print(str(t_map[x]))


def test_monty():
    """蒙蒂霍尔悖论游戏"""
    thing = ['goat', 'goat', 'car']
    # 洗牌算法随机生成
    for i in range(3):
        x1 = random.randint(0, 2)
        x2 = random.randint(0, 2)
        thing[x1], thing[x2] = thing[x2], thing[x1]
    car_num = thing.index('car')
    choice = int(input('请选择一个门:'))
    if choice == car_num:  # 是
        # 输出out number,不等于car对应的值
        while True:
            num1 = random.randint(0, 2)
            if num1 != car_num:
                break
    else:  # 不是
        # 输出另一个goat的数字
        num1 = 3 - choice - car_num
        # 主持人告诉一个山羊的位置
    print('"山羊"在这门后:' + str(num1))
    # 主持人询问是否换门
    else_number = 3 - num1 - choice
    confirm_choice = input('确定换到 ' + str(else_number) + '?(y/n)')
    if confirm_choice == 'y':
        choice2 = else_number
    else:
        choice2 = choice
    # 最终选择的门是否为car
    if choice2 == car_num:
        print('你获得了汽车')
    else:
        print('你什么都没有，山羊都不愿意跟你走')
    return


if __name__ == '__main__':
    main()
