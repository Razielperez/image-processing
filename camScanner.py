

import cv2
import numpy as np
import math
from matplotlib import pyplot as plt


def binarization(img):# פונקציה שמבצעת בינאריזציה על התמונה לפי OTSU
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgGray, (61, 61), 0)
    otsu_threshold, image_result = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
    return image_result
def findMaxContour(img):# פנוקציה שמוצאת את הcontur הגדול ביותר לפי שטח
    imgBin = binarization(img)
    (cnts, _) = cv2.findContours(imgBin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxArea=max(cv2.contourArea(c) for c in cnts)
    maxCnt=list(c for c in cnts if cv2.contourArea(c)==maxArea)[0]
    return maxCnt
def createMetrix(img):# פונקציה שממירה את הCUNTOR ללמערך של ארבע נקודות ובונה מטריצה טרנספורמציה
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
def camScanner(path):# פונקציה שמבצעת טרנספורמציה
    img = cv2.imread(path, 1)
    imgCopy = img.copy()

    M,h,w=createMetrix(img)
    dst=cv2.warpPerspective(imgCopy, M, (w, h))
    #plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)), plt.title('dst')
    # plt.show()
    cv2.imwrite('output\camScanner.jpg', cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
    return 'output\camScanner.jpg'






