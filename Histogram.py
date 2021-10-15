# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt



def HistogramComputation(image):
    imageHeight=image.shape[0]
    imageWidth=image.shape[1]
    
    Histogram = np.zeros([256],np.int32)
    
    for x in range(0,imageHeight):
        for y in range(0,imageWidth):
            Histogram[image[x,y]]+=1
    return Histogram

def HistogramDisplay(Histogram):
    plt.figure()
    plt.title("GrayScale image histogram")
    plt.xlabel("GrayScaleValue")
    plt.ylabel("Pixel count")
    plt.xlim([0,256])
    plt.plot(Histogram)
    plt.show()

def main():
#Show Histogram from scratch
#GrayScale
    GrayScaleImage=cv.imread("Colorful.jpg")
    ColorImage=cv.imread("Colorful.jpg")
    Histogram = HistogramComputation(GrayScaleImage)
    HistogramDisplay(Histogram)
#Show original img
    cv.imshow('Original Image',ColorImage)
    cv.waitKey(0)
#Color:
    his1 = HistogramComputation(ColorImage[:,:,0])
    his2 = HistogramComputation(ColorImage[:,:,1])
    his3 = HistogramComputation(ColorImage[:,:,2])
    plt.subplot(221),plt.plot(his1),plt.plot(his2),plt.plot(his3)
    plt.xlim([0,256])
    plt.show()
#Using calcHist function in openCV
#Gray Image:
    hisFunc=cv.calcHist([GrayScaleImage],[0],None,[256],[0,256])
    plt.plot(hisFunc)
    plt.show()
#Color Image:
    hist1 = cv.calcHist([ColorImage],[0],None,[256],[0,256])
    hist2 = cv.calcHist([ColorImage],[1],None,[256],[0,256])
    hist3 = cv.calcHist([ColorImage],[2],None,[256],[0,256])
    
    plt.subplot(221),plt.plot(hist1),plt.plot(hist2),plt.plot(hist3)
    plt.xlim([0,256])
    plt.show()
    
if __name__=='__main__':
    main()
