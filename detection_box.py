#!C:\pythonCode
# -*- coding: utf-8 -*-
# @Time : 2022/8/22 11:27
# @Author : duweidong
# @File : utils_duweidong.py
# @Software: PyCharm

"""
some functions of detection box
"""

import cv2
from typing import List, Dict, Tuple


def plot_one_rotated_box(img_bgr: np.ndarray, rotated_box: List, text: str = None) -> None:
    """
    plot the rotated box on the 3 channels image

    Args:
        img_bgr: the 3 channels image
        rotated_box: [[center_x, center_y], [w, h], angle], this rotated box is returned from cv2.minAreaRect()
        text: the text of rotated box

    Returns:
        img_bgr: the 3 channels image

    """
    center, size, angle = rotated_box[0], rotated_box[1], rotated_box[2]
    center, size = tuple(map(int, center)), tuple(map(int, size))

    w = size[0]
    h = size[1]
    x = center[0]
    y = center[1]
    angelPi = (angle / 180) * math.pi

    x1 = x + (w / 2) * math.cos(angelPi) - (h / 2) * math.sin(angelPi)
    y1 = y + (w / 2) * math.sin(angelPi) + (h / 2) * math.cos(angelPi)

    x2 = x + (w / 2) * math.cos(angelPi) + (h / 2) * math.sin(angelPi)
    y2 = y + (w / 2) * math.sin(angelPi) - (h / 2) * math.cos(angelPi)

    x3 = x - (w / 2) * math.cos(angelPi) + (h / 2) * math.sin(angelPi)
    y3 = y - (w / 2) * math.sin(angelPi) - (h / 2) * math.cos(angelPi)

    x4 = x - (w / 2) * math.cos(angelPi) - (h / 2) * math.sin(angelPi)
    y4 = y - (w / 2) * math.sin(angelPi) + (h / 2) * math.cos(angelPi)
    # cv2.circle(img, center, 2, (0, 0, 0), thickness=2)
    cv2.line(img_bgr, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 250), thickness=2)
    cv2.line(img_bgr, (int(x2), int(y2)), (int(x3), int(y3)), (0, 0, 250), thickness=2)
    cv2.line(img_bgr, (int(x3), int(y3)), (int(x4), int(y4)), (0, 0, 250), thickness=2)
    cv2.line(img_bgr, (int(x4), int(y4)), (int(x1), int(y1)), (0, 0, 250), thickness=2)

    return img_bgr