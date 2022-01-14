import cv2
import numpy as np
from matplotlib import pyplot as plt

#Range of colors according to HSV
HSV_RANGES = {
    'red': [
        {
            'lower': np.array([0, 39, 64]),
            'upper': np.array([20, 255, 255])
        },
        {
            'lower': np.array([161, 39, 64]),
            'upper': np.array([180, 255, 255])
        }
    ],
    'yellow': [
        {
            'lower': np.array([21, 39, 64]),
            'upper': np.array([40, 255, 255])
        }
    ],
    'green': [
        {
            'lower': np.array([41, 39, 64]),
            'upper': np.array([80, 255, 255])
        }
    ],
    'cyan': [
        {
            'lower': np.array([81, 39, 64]),
            'upper': np.array([100, 255, 255])
        }
    ],
    'blue': [
        {
            'lower': np.array([101, 39, 64]),
            'upper': np.array([140, 255, 255])
        }
    ],
    'violet': [
        {
            'lower': np.array([141, 39, 64]),
            'upper': np.array([160, 255, 255])
        }
    ],
    'black': [
        {
            'lower': np.array([0, 0, 0]),
            'upper': np.array([180, 255, 63])
        }
    ],
    'gray': [
        {
            'lower': np.array([0, 0, 64]),
            'upper': np.array([180, 38, 228])
        }
    ],
    'white': [
        {
            'lower': np.array([0, 0, 229]),
            'upper': np.array([180, 38, 255])
        }
    ]
}

#A function that produces a mask according to the selected colors
def create_mask(hsv_img, colors):
    mask = np.zeros((hsv_img.shape[0], hsv_img.shape[1]), dtype=np.uint8)

    for color in colors:
        for color_range in HSV_RANGES[color]:
            # noinspection PyUnresolvedReferences
            mask += cv2.inRange(
                hsv_img,
                color_range['lower'],
                color_range['upper']
            )
    return mask

#A function that removes the selected colors according to the created mask
def clearColor(path,colors):
    img = cv2.imread(path,1)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = create_mask(img_hsv, colors)
    mask=cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    res = cv2.bitwise_or(img, mask)
    cv2.imwrite('output\clearColor.jpg', res)
    return 'output\clearColor.jpg'
