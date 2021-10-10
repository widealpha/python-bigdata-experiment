import random

if __name__ == '__main__':
    print("学号:2020328704   姓名:吴昀霏")
    str1 = input('请输入随机字符串:')
    print('输入的随机产生的字符串是:' + str1)
    index = random.randint(0, len(str1) - 1)
    print('随机产生的索引值是:%d' % index)
    str1 = str1[:index] + str1[index + 1:]
    print(('删除随机索引为%d的字符串结果是' % index) + str1)
