"""
Python绘制等高线
求求了,复制的时候多少改点东西吧,打声招呼也行啊 by-201900301053
"""
import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import interpolate


def get_mode():
    print('===================================================')
    print('请输入想要显示的模式:\n'
          '1.显示3D高程图\n'
          '2.显示3D等高线图\n'
          '3.显示2D等高线图\n'
          '4.显示2D等高线图(无色彩填充)\n'
          '5.显示1与2的综合图\n\n'
          '默认显示3D等高线图')
    mode = input('===================================================\n')
    print('正在计算,请稍后...')
    return mode


def init_data():
    return pd.read_excel('./data1.xlsx', header=None, nrows=874)


def solve(excel, mode):
    fig = plt.figure()
    x = np.linspace(0, 50 * 874, 874)
    y = np.linspace(0, 50 * 1165, 1165)
    z = np.array(excel.values).astype(float).T

    # 如果不追求下一步插值的效果,可以将8740与11650按比例同步缩小,减少插值时间和内存占用
    xi = np.linspace(0, 50 * 874, 8740)
    yi = np.linspace(0, 50 * 1165, 11650)

    f = interpolate.interp2d(x, y, z, kind='cubic')  # 用插值均匀数据
    Z = f(xi, yi)
    X, Y = np.meshgrid(xi, yi)

    if mode == '1':
        """3D高程图"""
        ax = fig.gca(projection='3d')
        surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
    elif mode == '2':
        """3D等高线"""
        ax = fig.gca(projection='3d')
        plt.contourf(X, Y, Z)
        # 画等高线
        contour = plt.contour(X, Y, Z)
        plt.clabel(contour, fontsize=10)
    elif mode == '3':
        """2D等高线"""
        plt.contourf(X, Y, Z)
        # 画等高线
        contour = plt.contour(X, Y, Z)
        plt.clabel(contour, fontsize=10)
    elif mode == '4':
        """2D等高线(无色彩填充)"""
        contour = plt.contour(X, Y, Z)
        plt.clabel(contour, fontsize=10)
    elif mode == '5':
        """显示1与2的结合"""
        ax = fig.gca(projection='3d')
        plt.contourf(X, Y, Z)
        # 画等高线
        contour = plt.contour(X, Y, Z)
        plt.clabel(contour, fontsize=10)
        surf = ax.plot_surface(X, Y, Z, cmap='coolwarm')
    else:
        """默认3D等高线"""
        ax = fig.gca(projection='3d')
        plt.contourf(X, Y, Z)
        # 画等高线
        contour = plt.contour(X, Y, Z)
        plt.clabel(contour, fontsize=10)
    print('计算完成')
    filename = 'image_' + mode + '_' + str(random.randint(1, 100)) + '.png'
    fig.savefig(filename, dpi=100)
    plt.show()
    return filename


def main():
    excel = init_data()
    mode = get_mode()
    solve(excel, mode)


if __name__ == '__main__':
    main()
