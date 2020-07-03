import cv2 as cv
import numpy as np
import math

def read_image(path):
	img = cv.imread(path)
	gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
	arr=np.asarray(gray_img)
	X = arr.shape[1]
	Y = arr.shape[0]
	
	return arr,X,Y

def mask3x3(array,X,Y):
    mask=[]
    for i in range(1,Y-1):
        for j in range(1,X-1):
            mask.append(array[i-1:i+2,j-1:j+2])
            
    return mask 

def mean_std_value(arr,bar):
    means = []
    stds = []
    length = len(arr)
    for i in range(length):
        if i%10000 == 0:
            bar['value'] = 30+i*(70/length)
            bar.update()
        
        sum_mask = 0
        mean_mask = 0
        std_mask = 0
        
        for j in range(9):
            sum_mask = sum_mask + arr[i][int(j/3),j%3]
            
        mean_mask = sum_mask / 9
        sum_mask = 0
        
        for k in range(9):
            a = (arr[i][int(k/3),k%3]-mean_mask)
            sum_mask = sum_mask + a*a
        
        std_mask = math.sqrt(sum_mask / 9)
        stds.append(std_mask)
        means.append(mean_mask)
       
    return means,stds     
