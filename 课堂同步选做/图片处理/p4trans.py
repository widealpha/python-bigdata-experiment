# -*- coding: utf-8 -*-

# python+opencv传统图像方法对仿射变换的校正
# https://zhuanlan.zhihu.com/p/272889629
# pip install --upgrade numpy==1.19.3
# pip install opencv-python scipy imutils
# https://docs.opencv.org/4.5.1/d6/d00/tutorial_py_root.html

import cv2
from imutils.perspective import four_point_transform
import numpy as np


# 透视矫正
def perspective_transformation(img):
    # 读取图像，做灰度化、高斯模糊、膨胀、Canny边缘检测
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    dilate = cv2.dilate(blurred, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    # edged = cv2.Canny(dilate, 75, 200)
    edged = cv2.Canny(dilate, 73, 200, 3)

    # cv2.namedWindow("enhanced", 0)
    # cv2.resizeWindow("enhanced", 1280, 960)
    # cv2.imshow("enhanced", edged)
    # cv2.waitKey(0)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if imutils.is_cv2() else cnts[1]  # 判断是OpenCV2还是OpenCV3
    # if cv4:
    cnts = cnts[0]
    docCnt = None

    # 确保至少找到一个轮廓
    if len(cnts) > 0:
        # 按轮廓大小降序排列
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
        for c in cnts:
            # 近似轮廓
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.02 * peri, True)
            # 如果我们的近似轮廓有四个点，则确定找到了纸
            if len(approx) == 4:
                docCnt = approx
                break

    # 对原始图像应用四点透视变换，以获得纸张的俯视图
    paper = four_point_transform(img, docCnt.reshape(4, 2))
    return paper


def test(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)

    comma = cv2.imread("comma.png")
    r, comma = cv2.threshold(cv2.cvtColor(comma, cv2.COLOR_BGR2GRAY), 200, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow("a", comma)

    template = comma
    result = template_match(comma, thresh)
    print(result)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, contours, -1, (0, 0, 0), 1, 1)

    areas = []
    for c in range(len(contours)):
        areas.append(cv2.contourArea(contours[c]))
    arr = np.array(areas)
    max_elements = arr.argsort()[-3:][::-1]
    for max_id in max_elements:
        x, y, w, h = cv2.boundingRect(contours[max_id])

    cv2.imshow("test", image)
    cv2.waitKey(0)


def template_match(template, src):
    # 获得模板图片的高宽尺寸
    w, h = template.shape[:2]
    # 执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    result = cv2.matchTemplate(src, template, cv2.TM_CCOEFF_NORMED)
    # 尝试逗号分割
    threshold = 0.6
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(src, pt, (pt[0] + w, pt[1] + h), (255, 255, 255), 1)

    cv2.imshow("MatchResult----MatchingValue", src)


def main():
    image = cv2.imread('p4-test1.jpg')
    img = perspective_transformation(image)

    # test(img)
    # 旋转
    img_trans = cv2.transpose(img)
    # 取镜像
    img = cv2.flip(img_trans, 0)

    # test(img)

    cv2.imshow('enhanced', img)

    # 写入文件
    cv2.imwrite("p4-test1-trans-ok.jpg", img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
