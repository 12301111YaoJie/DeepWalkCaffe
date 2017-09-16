#!/usr/bin/env python
# -*- coding: utf-8 -*-


import cv2  
import numpy as np  
import Image  
import cv2.cv as cv  
import time

def image_joint(image_list,opt):#opt= vertical ,horizon  
	image_num=len(image_list)  
	image_size=image_list[0].size  
	height=image_size[1]  
	width=image_size[0]  
	  
	if opt=='vertical':  
	    new_img=Image.new('RGB',(width,image_num*height),255)  
	else:  
	    new_img=Image.new('RGB',(image_num*width,height),255)  
	x=y=0  
	count=0  
	for img in image_list:  
	      
	    new_img.paste(img,(x,y))  
	    count+=1  
	    if opt=='horizontal':  
		x+=width  
	    else : y+=height  
	return new_img  





def image_flow(imagepath ,newimagepath, image1 , image2 ):

	imagepath = '/home/yao/django_test/deepwalk/deepwalk/pic/'
	newimagepath = '/home/yao/django_test/deepwalk/deepwalk/flow/'
	image1 = '1.jpg'
	image2 = '3.jpg'

	start_img1 = Image.open(imagepath + image1)  
	later_img1 = Image.open(imagepath + image2)

	start_img=np.array(start_img1)  
	later_img=np.array(later_img1)  

	print(start_img.shape)
	print(later_img.shape)
	start = cv2.cvtColor(start_img,cv2.COLOR_BGR2GRAY)  
	later = cv2.cvtColor(later_img,cv2.COLOR_BGR2GRAY)
	flow = cv2.calcOpticalFlowFarneback(start, later, 0.3, 3, 20, 3, 5, 1.2, 0, 0 )

	hsv = np.zeros_like(start_img) 
	hsv[...,1] =255
	mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])  
	hsv[...,0] = ang*180/np.pi/2  
	hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)  
	RGB= cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)  
	cv2.imwrite(newimagepath + image1,RGB) 



if __name__ == "__main__":
	image_flow ('./pic/' , './flow/', '1.jpg' , '3.jpg')
