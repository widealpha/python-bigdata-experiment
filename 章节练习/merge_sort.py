"""文件于experience有一份同样的备份"""

import shutil
from os import remove, listdir

i = 0


def main():
    split_file('./example/a.txt')
    merge()
    return


def split_file(filename):
    """分割文件并进行初始化排序"""
    global i
    in_file = open(filename)
    # 防止内存溢出每次读取100000行
    block = in_file.readlines(100000)
    block.sort()
    while len(block) != 0:
        f = open('./result/split/' + str(i))
        f.writelines(block)
        block = in_file.readlines(100000)
        block.sort()
        i = i + 1
    in_file.close()


def merge():
    """利用归并排序思想实现外排序"""
    global i
    now = 0
    result_file = open('./result/sorted.txt', 'w+')
    split_dir = listdir('./result/split')
    split_dir.sort()  # 按照文件名排序
    if len(split_dir) == 1:  # 只有一个文件的情况,直接把文件写入
        result_file.writelines(open(split_dir[0]).readlines())
        result_file.close()
        return

    while len(split_dir) > 1:
        f1 = open(split_dir[now])
        f2 = open(split_dir[now + 1])
        output = open('./result/split/' + str(i), 'w+')
        now += 2
        i += 1
        s1 = f1.readline()
        s2 = f2.readline()
        while s1 and s2:  # 较小写入，升序排序
            if s1 < s2:
                output.write(s1)
                s1 = f1.readline()
            else:
                output.write(s2)
                s2 = f2.readline()
        if s1:  # 一个文件已经为空，剩下的直接写入就好
            f2.close()
            output.write(s1)
            output.writelines(f1.readlines())
            f1.close()
        if s2:
            f1.close()
            output.write(s2)
            output.writelines(f2.readlines())
            f2.close()
        # 归并结束删除文件
        remove(f1.name)
        remove(f2.name)
        split_dir = listdir('./result/split')
        split_dir.sort()  # 按照文件名排序
        output.close()

    # 只剩一个文件就是归并结果
    shutil.move('./result/split/' + str(i - 1), './result/sorted.txt')


if __name__ == '__main__':
    main()
