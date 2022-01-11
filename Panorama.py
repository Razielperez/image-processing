
import cv2
import sys
import os
import numpy as np
from matplotlib import pyplot as plt


#A function that checks the resolution of the two images and compares their height while maintaining the aspect ratio
def resize(img_l,img_r):
    height1 = img_l.shape[0]
    height2 = img_r.shape[0]
    if (height1 > height2):
        img_r=cv2.resize(img_r, (0,0), fx=(height1/height2), fy=(height1/height2))
    elif (height1<height2):
        img_l = cv2.resize(img_l, (0, 0), fx=(height2/height1), fy=(height2/height1))
    gray1=cv2.cvtColor(img_l, cv2.COLOR_BGR2GRAY)
    gray2=cv2.cvtColor(img_r, cv2.COLOR_BGR2GRAY)
    return gray1,gray2

#A function that finds key points in each image and their descriptions
def ORB(img_l,img_r):
    img_l,img_r=resize(img_l,img_r)
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(img_l, None)
    keypoints2, descriptors2 = orb.detectAndCompute(img_r, None)
    return keypoints1, descriptors1,keypoints2, descriptors2

#A function that finds the array of matches between the key points in the two images
def bfMatcher(img_l,img_r):
    keypoints1, descriptors1, keypoints2, descriptors2=ORB(img_l,img_r)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)
    matches = sorted(matches, key=lambda x: x.distance)[:int(len(matches)*0.2)]
    #showMatch(img_l,img_r,keypoints1,keypoints1,matches)
    return keypoints1,keypoints2,matches

#A function that draws lines between the found key points and displays them
def showMatch(img_l,img_r,keypoints1,keypoints2,matches):
    imMatches = cv2.drawMatches(img_l, keypoints1, img_r, keypoints2,matches, None)
    imMatches=cv2.cvtColor(imMatches, cv2.COLOR_BGR2RGB)
    plt.imshow(imMatches), plt.show()

# Function that finds the homography matrix is a 3 x 3 matrix that represents a transformation
# 2D. This transformation maps points from one plane (right image) to another plane (left image)
def matrixHomography(img_l,img_r):
    keypoints1, keypoints2,matches=bfMatcher(img_l,img_r)
    src_pts = np.float32([keypoints1[m.queryIdx].pt for m in matches])
    dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in matches])
    H, _ = cv2.findHomography(dst_pts,src_pts, cv2.RANSAC)
    return H

# Function that performs transformation according to matrix H
def transformation(img_l,img_r):
    height_panorama=img_l.shape[0]
    width_panorama=img_l.shape[1]+img_r.shape[1]
    H=matrixHomography(img_l,img_r)
    res=cv2.warpPerspective(img_r, H, (width_panorama, height_panorama))
    #plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB)),plt.title("transformation"), plt.show()
    return res

#A function that "sews" the two images and cuts the black pieces
def sewAndCut(img_l,img_r):
    h1,w1=img_l.shape[:2]
    res=transformation(img_l,img_r)
    res[:h1,:w1,:]=img_l[:,:,:]
    #plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB)), plt.title("sew"), plt.show()
    return cut(res)

#A function that cuts the black parts
def cut(img):
#-------------------Find the square that blocks the image----------------
    h,w=img.shape[:2]
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.medianBlur(imgGray,11)
    _, imgBin = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    (cnts, _) = cv2.findContours(imgBin, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    maxCnt=max(cnts,key=lambda c:cv2.contourArea(c))
    epsilon = 0.01 * cv2.arcLength(maxCnt, True)
    approx = cv2.approxPolyDP(maxCnt, epsilon, True)

#--------------------Finding the boundaries of the image-----------------
    limitCol=min(approx[2][0][0],approx[3][0][0])#Finding the boundary that blocks the columns
    limitRowMax=h
    limitRowMin=0
    for i in range(h//2,h):#Find the smallest row that does not contain a black part
        if 0 in imgBin[i][:limitCol-1]:
            limitRowMax=i
            break
    for i in range((h//2)+1,0):# Find the largest row that does not contain a black part
        if 0 in imgBin[i][:limitCol-1]:
            limitRowMin=i
            break
    res=img[limitRowMin:limitRowMax,:limitCol]
    return (res)

def panorama(path_img_l,path_img_r):
    img_l = cv2.imread(path_img_l, 1)
    img_r = cv2.imread(path_img_r, 1)
    res=sewAndCut(img_l,img_r)
    cv2.imwrite('output\panorama.jpg', res)
    return 'output\panorama.jpg'








