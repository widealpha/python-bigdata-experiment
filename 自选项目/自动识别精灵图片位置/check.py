import json
import os

import cv2
import numpy as np
from matplotlib import pyplot as plt


def main():
    img_dir = os.listdir('./origin')
    for filename in img_dir:
        try:
            print(filename)
            s = filename.split('.')
            json_file = open("./result/" + s[0] + '.json', mode='r+')
            spirit_map = json.loads(json_file.read())
            eye_map = spirit_map['eyes']
            mouth_map = spirit_map['mouth']
            # print(spirit_map)
            image = cv2.imread("./origin/" + filename, cv2.IMREAD_UNCHANGED)
            eyes = crop(image, [eye_map['position'][2], eye_map['position'][3],
                                eye_map['position'][2] + eye_map['blockSize'][0],
                                eye_map['position'][3] + eye_map['blockSize'][1]])
            mouth = crop(image, [mouth_map['position'][2], mouth_map['position'][3],
                                 mouth_map['position'][2] + mouth_map['blockSize'][0],
                                 mouth_map['position'][3] + mouth_map['blockSize'][1]])
            eyes_width = eye_map['blockSize'][0]
            eyes_height = eye_map['blockSize'][1]
            mouth_width = mouth_map['blockSize'][0]
            mouth_height = mouth_map['blockSize'][1]
            eye_map = spirit_map['character']['children']['eyes']
            image[eye_map[3]:eye_map[3] + eyes_height, eye_map[2]:eye_map[2] + eyes_width] = eyes
            mouth_map = spirit_map['character']['children']['mouth']
            image[mouth_map[3]:mouth_map[3] + mouth_height, mouth_map[2]:mouth_map[2] + mouth_width] = mouth
            cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
            cv2.imwrite('./check/' + filename, image)
        except BaseException as e:
            print(e)
            continue


def crop(img, boundaries):
    min_x, min_y, max_x, max_y = boundaries
    min_x = int(min_x)
    min_y = int(min_y)
    max_x = int(max_x)
    max_y = int(max_y)
    return img[min_y:max_y, min_x:max_x].copy()


if __name__ == '__main__':
    main()
