import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("C:/Windows/System32/ad-detection/result/shot-boundary/15140.png",0)
plt.hist(img.ravel(),256,[0,256]); plt.show()



