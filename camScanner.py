

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

#A function that binarizes an image according to OTSU
def binarization(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgGray, (61, 61), 0)
    otsu_threshold, image_result = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    return image_result

# Function that finds the largest contour by area
def findMaxContour(img):
    imgBin = binarization(img)
    (cnts, _) = cv2.findContours(imgBin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea=max(cv2.contourArea(c) for c in cnts)
    maxCnt=list(c for c in cnts if cv2.contourArea(c)==maxArea)[0]
    return maxCnt

# A function that converts the cuntor to a four-point array and builds a transformation matrix
def createMetrix(img):
    cnt=findMaxContour(img)

    epsilon = 0.05 *cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    pts1=np.float32(list(approx[i][0] for i in range(len(approx))))
    h, w = calcHeightAndWidth(pts1)
    difultPts2 = [[0, 0], [0, h], [w, h], [w, 0]]
    pts2 =np.float32(difultPts2)if pts1[1][1] > pts1[3][1] else np.float32(rotate(difultPts2,-1))

    M = cv2.getPerspectiveTransform(pts1, pts2)
    print(h,w)
    return M,h,w

def rotate(l, n):
     return l[n:] + l[:n]

#A function that calculates the height and width of the document
def calcHeightAndWidth(arr):
    dic1=int(math.dist(arr[0],arr[1]))
    dic2=int(math.dist(arr[1],arr[2]))
    if dic1>dic2:
        h=dic1
        w=dic2
    else:
        h = dic2
        w = dic1
    return h,w

# A function that performs a transformation    
def camScanner(path):
    img = cv2.imread(path, 1)
    imgCopy = img.copy()

    M,h,w=createMetrix(img)
    dst=cv2.warpPerspective(imgCopy, M, (w, h))
    cv2.imwrite('output\camScanner.jpg', cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    return 'output\camScanner.jpg'






