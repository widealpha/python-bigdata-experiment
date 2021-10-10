import json
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt

info = {
    "image": {
        "src": "cocoa_1d7a76441d212143c4ef8a1772eaff5d.png",
        "size": [1018, 570]
    },
    "character": {
        "position": [287, 570, 0, 0],
        "blockSize": [287, 570],
        "children": {
            "eyes": [125, 90, 53, 98],
            "mouth": [52, 24, 83, 190]
        }
    },
    "eyes": {
        "position": [650, 540, 288, 0],
        "blockSize": [125, 90]
    },
    "mouth": {
        "position": [104, 552, 914, 0],
        "blockSize": [52, 24]
    }
}


def main():
    # filename = 'cocoa_1d7a76441d212143c4ef8a1772eaff5d.png'
    img_dir = os.listdir('./origin')
    for filename in img_dir:
        print(filename)
        img = get_img("./origin/" + filename)
        plt.imshow(img)
        # cv2.imshow('BGR', img)
        # cv2.waitKey(0)
        plt.figure("Image")  # 图像窗口名称
        plt.imshow(img)
        plt.axis('on')  # 关掉坐标轴为 off
        plt.title('image')  # 图像题目
        plt.show()

        process_img_line(img, filename)

        s = filename.split('.')
        json_file = open("./result/" + s[0] + 'cocoa_010007.json', mode='w+')
        print(json.dumps(info))
        json_file.write(json.dumps(info))
        json_file.flush()
        json_file.close()

        cv2.waitKey(0)


def single_main():
    filename = '17.png'
    print(filename)
    img = get_img(filename)
    plt.imshow(img)
    # cv2.imshow('BGR', img)
    # cv2.waitKey(0)
    plt.figure("Image")  # 图像窗口名称
    plt.imshow(img)
    plt.axis('on')  # 关掉坐标轴为 off
    plt.title('image')  # 图像题目
    plt.show()
    process_img_line(img, filename)
    s = filename.split('.')
    json_file = open('single.json', mode='w+')
    print(json.dumps(info))
    json_file.write(json.dumps(info))
    json_file.flush()
    json_file.close()
    cv2.waitKey(0)


def get_img(filename):
    image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    info['image']['src'] = filename
    info['image']['size'] = [image.shape[1], image.shape[0]]
    # cv2.imshow('name', image)
    mask = image[:, :, 3] == 0  # we find all the places where background is transperent
    image[mask] = [255, 255, 255, 255]  # we replace that transperent background with white
    # background
    return cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)  # convert it to 3 channel


# 初步处理图片确定位置,最小斜矩形
# def process_img(img, filename):
#     character_place = 0
#     eyes_place = 0
#     mouth_place = 0
#     image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, thresh = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY_INV)
#     contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     # cv2.drawContours(image, contours, -1, (255, 255, 255), 1, 1)
#
#     # min_w = 1000
#     # max_w = 0
#     # sub_max_w = 0
#     # for c in range(len(contours)):
#     #     print(str(contours))
#     areas = []
#     for c in range(len(contours)):
#         areas.append(cv2.contourArea(contours[c]))
#     arr = np.array(areas)
#     max_elements = arr.argsort()[-3:][::-1]
#     for max_id in max_elements:
#         max_rect = cv2.minAreaRect(contours[max_id])
#         box0 = cv2.boundingRect(contours[max_id])
#         rec = cv2.rectangle(img, box0, (0, 0, 255), 1, 1)
#         cv2.imshow('rec', rec)
#         # 得到矩形的坐标
#         box = cv2.boxPoints(max_rect)
#         # 标准化坐标到整数
#         box = np.int0(box)
#         # 如果x据左边很近认为是人物(有问题再改)
#         if box[0][0] < 30:
#             info['character']['position'] = [box[2][0] - box[0][0], box[2][1] - box[0][1], box[0][0], box[0][1]]
#             info['character']['blockSize'] = [box[2][0] - box[0][0], box[2][1] - box[0][1]]
#             character_place = crop(image, [box[0][0], box[0][1], box[2][0], box[2][1]])
#         # 面积倒数第三大的矩形是嘴巴
#         elif max_id == max_elements[2]:
#             info['mouth']['position'] = [box[2][0] - box[0][0], box[2][1] - box[0][1], box[0][0], box[0][1]]
#             info['mouth']['blockSize'] = [box[2][0] - box[0][0], box[2][1] - box[0][1]]
#             mouth_place = crop(image, [box[0][0], box[0][1], box[2][0], box[2][1]])
#         # 距离左边远一点且面积较大的是眼睛
#         else:
#             info['eyes']['position'] = [box[2][0] - box[0][0], box[2][1] - box[0][1], box[0][0], box[0][1]]
#             info['eyes']['blockSize'] = [box[2][0] - box[0][0], box[2][1] - box[0][1]]
#             eyes_place = crop(image, [box[0][0], box[0][1], box[2][0], box[2][1]])
#         # 画出边界
#         # cv2.drawContours(image, [box], 0, (0, 0, 255), 1, 1)
#     # find_eyes(eyes_place, character_place)
#     # find_mouth(mouth_place, character_place)
#     # cv2.imshow('character', character_place)
#     # cv2.imwrite('r_' + filename, character_place)
#     cv2.imshow("img", image)
#     return image


# 初步处理图片确定位置,最小水平矩形
def process_img_line(img, filename):
    character_place = 0
    eyes_place = 0
    mouth_place = 0
    rec = img
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 230, 255, cv2.THRESH_BINARY_INV)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    areas = []
    for c in range(len(contours)):
        areas.append(cv2.contourArea(contours[c]))
    arr = np.array(areas)
    max_elements = arr.argsort()[-3:][::-1]
    for max_id in max_elements:
        x, y, w, h = cv2.boundingRect(contours[max_id])
        box = [x, y, x + w, y + h]
        # 如果x据左边很近认为是人物(有问题再改)
        if box[0] < 30:
            if eyes_place is not int:
                info['character']['position'] = [info['character']['position'][0], img.shape[0], 0, 0]
                info['character']['blockSize'] = [info['character']['position'][0], img.shape[0]]
                rec = cv2.rectangle(img, (0, 0), (x + w, y + h), (0, 0, 255), 1, 1)
            else:
                info['character']['position'] = [w, h, 0, 0]
                info['character']['blockSize'] = [w, h]

            character_place = crop(image, [0, 0, x + w, y + h])
        # 面积倒数第三大的矩形是嘴巴
        elif max_id == max_elements[2]:
            info['mouth']['position'] = [w, h, x, y]
            # info['mouth']['blockSize'] = [w, h]
            mouth_place = crop(image, box)
            rec = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1, 1)
        # 距离左边远一点且面积较大的是眼睛
        else:
            info['eyes']['position'] = [w, h, x, y]
            # info['eyes']['blockSize'] = [w, h]
            info['character']['blockSize'][0] = x - 1
            info['character']['position'][0] = x - 1
            eyes_place = crop(image, box)
            rec = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1, 1)
            if character_place is not int:
                rec = cv2.rectangle(img, (0, 0), (x - 1, img.shape[0]), (0, 0, 255), 1, 1)

    # find_eyes(eyes_place, character_place)
    # find_mouth(mouth_place, character_place)
    cv2.imwrite("./check/" + 'r_' + filename, character_place)
    return image


def crop(img, boundaries):
    min_x, min_y, max_x, max_y = boundaries
    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)
    return img[min_y:max_y, min_x:max_x].copy()


def find_eyes(eyes_place, character_place):
    width = eyes_place.shape[1] + 1
    height = eyes_place.shape[0] + 1
    row = 6
    col = 2
    try:
        row, col = input('请输入眼睛的行数和列数(空格分开):\n').rstrip().split(' ')
    except BaseException:
        row, col = input('请输入眼睛的行数和列数(空格分开):\n').rstrip().split(' ')
    row, col = int(row), int(col)
    i, j = 0, 0
    template = crop(eyes_place,
                    [i / col * width, j / row * height, (i + 1) / col * width, (j + 1) / row * height])
    array = template_match(template, character_place)
    info['eyes']['blockSize'] = [array[0], array[1]]
    info['character']['children']['eyes'] = array.copy()

    # cv2.imshow('',crop(img, [i / col * width, j / row * height, (i + 1) / col * width, (j + 1) / row * height]))
    # for i in range(4):
    #     for j in range(6):
    #         tmp = crop(img, [i / col * width, j / row * height, (i + 1) / col * width, (j + 1) / row * height])
    #


def find_mouth(mouth_place, character_place):
    width = mouth_place.shape[1] + 1
    height = mouth_place.shape[0] + 1
    row = 11
    col = 1
    try:
        row, col = input('请输入嘴巴的行数和列数(空格分开):\n').rstrip().split(' ')
    except Exception:
        row, col = input('请输入嘴巴的行数和列数(空格分开):\n').rstrip().split(' ')
    row, col = int(row), int(col)
    i, j = 0, 0
    template = crop(mouth_place,
                    [i / col * width, j / row * height, (i + 1) / col * width, (j + 1) / row * height])
    array = template_match(template, character_place)
    info['mouth']['blockSize'] = [array[0], array[1]]
    info['character']['children']['mouth'] = array.copy()


def template_match(template, src):
    # 获得模板图片的高宽尺寸
    t_height, t_width = template.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(src, template, cv2.TM_SQDIFF_NORMED)
    # 归一化处理
    cv2.normalize(result, result, 0, 1, cv2.NORM_MINMAX, -1)
    # 寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # 匹配值转换为字符串
    # 对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    # 对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    # 绘制矩形边框，将匹配区域标注出来
    # min_loc：矩形定点
    # (min_loc[0]+t_width,min_loc[1]+t_height)：矩形的宽高
    # (0,0,225)：矩形的边框颜色；2：矩形边框宽度
    cv2.rectangle(src, min_loc, (min_loc[0] + t_width, min_loc[1] + t_height), (0, 0, 225), 2)
    # 显示结果,并将匹配值显示在标题栏上
    # str_val = str(min_val)
    # cv2.imshow("MatchResult----MatchingValue=" + str_val, img)
    return [t_width, t_height, min_loc[0], min_loc[1]]


if __name__ == '__main__':
    # main()
    single_main()
