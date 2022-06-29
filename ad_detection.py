import cv2
from matplotlib import pyplot as plt
import numpy as np
import os

thres=0.3
framelist = []
diff_list = []
total=0
num=0
shot_list=[]
shot_list_image=[]
ad_list=[]

path1="C:/Windows/System32/ad-detection/result/shot-boundary"
path2="C:/Windows/System32/ad-detection/result/ad-boundary"
class Frame:
    index=-1
    img= None
    diff=0
    hist=[]
    

cap = cv2.VideoCapture("TVshow_7.avi")
ret, frame = cap.read()
index = -1

while (cap.isOpened()):

        ret, frame = cap.read()
        if ret == False:
            break
        index += 1
        if index >=10000:
            break
        img = frame
        frame2 = Frame()
        frame2.index = index
        frame2.img = img.copy()
        framelist.append(frame2)



        img = cv2.blur(img, (5, 5)) 

        b, g, r = cv2.split(img)
        hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])  
        hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])  
        hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])  
        weight= [0.33,0.33,0.33]
        hist= weight[0]*hist_b +weight[1]* hist_g + weight[2]* hist_r
        frame2.hist = hist
        
        
        if len(framelist)>=2:
            frame3 =  framelist[len(framelist) - 2]
            newhist = frame3.hist
            diff = cv2.compareHist( hist, newhist, cv2.HISTCMP_BHATTACHARYYA )
            frame3.diff = diff
            diff_list.append(frame3.diff)
        
for i in range(0, len(framelist) - 1):
           
    if framelist[i].diff >= thres:
           cv2.imwrite(path1 + "/" + str(framelist[i].index) + ".png", framelist[i].img)
           shot_list.append(framelist[i].index)
           shot_list_image.append(framelist[i].img)


for k in range(0, len(shot_list) - 1):
    if shot_list(k+1)-shot_list(k)<=200:
          cv2.imwrite(path2 + "/" + str(shot_list[k]) + ".png", shot_list_image[k])
          ad_list.append(shot_list[k])



cap.release()


