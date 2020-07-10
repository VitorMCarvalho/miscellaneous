''''| Author: Jean Vitor de Paulo 
	| Date: 29/09/2018
	| Edited by Vitor Mendes Carvalho and Eduardo Alexandre for test -- remotion of skin (20/01/2020)
'''


import cv2 
import numpy as np
import matplotlib.pyplot as plt
import numpy as num
import numpy as np


class skinDetector(object):

	#class constructor
	def __init__(self, imageName, fundo):
		#self.image = cv2.imread(imageName)
		self.image = imageName
		self.fundo = fundo
		if self.image is None:
			print("IMAGE NOT FOUND")
			exit(1)                          
		#self.image = cv2.resize(self.image,(600,600),cv2.INTER_AREA)	
		imageblur = cv2.bilateralFilter(self.image,9,75,75)
		self.HSV_image = cv2.cvtColor(imageblur, cv2.COLOR_BGR2HSV)
		self.YCbCr_image = cv2.cvtColor(imageblur, cv2.COLOR_BGR2YCR_CB)
		self.binary_mask_image = self.HSV_image
#================================================================================================================================
	#function to process the image and segment the skin using the HSV and YCbCr colorspaces, followed by the Watershed algorithm
	def find_skin(self):
		self.__color_segmentation()
		self.__region_based_segmentation()
        
#================================================================================================================================
	#Apply a threshold to an HSV and YCbCr images, the used values were based on current research papers along with some
	# empirical tests and visual evaluation
	def __color_segmentation(self):
		lower_HSV_values = np.array([0, 40, 0], dtype = "uint8") #preto
		upper_HSV_values = np.array([25, 255, 255], dtype = "uint8") #amarelo

		lower_YCbCr_values = np.array((0, 138, 67), dtype = "uint8") #marrom-avermelhado
		upper_YCbCr_values = np.array((255, 173, 133), dtype = "uint8") #branco

        #A binary mask is returned. White pixels (255) represent pixels that fall into the upper/lower.
		mask_YCbCr = cv2.inRange(self.YCbCr_image, lower_YCbCr_values, upper_YCbCr_values)
		mask_HSV = cv2.inRange(self.HSV_image, lower_HSV_values, upper_HSV_values) 

		self.binary_mask_image = cv2.add(mask_HSV,mask_YCbCr)

#================================================================================================================================
	#Function that applies Watershed and morphological operations on the thresholded image
	def __region_based_segmentation(self):
		
		key = cv2.waitKey(1) & 0xFF #espera 1ms e verifica se alguma tecla foi pressionada
		
		#morphological operations		
		image_foreground = cv2.erode(self.binary_mask_image,None,iterations = 1)     	#remove noise
		dilated_binary_image = cv2.dilate(self.binary_mask_image,None,iterations = 10)   #The background region is reduced a little because of the dilate operation
		ret,image_background = cv2.threshold(dilated_binary_image,1,128,cv2.THRESH_BINARY)  #set all background regions to 128

		image_marker = cv2.add(image_foreground,image_background)   #add both foreground and backgroud, forming markers. The markers are "seeds" of the future image regions.
		image_marker32 = np.int32(image_marker) #convert to 32SC1 format

		cv2.watershed(self.image,image_marker32)
		m = cv2.convertScaleAbs(image_marker32) #convert back to uint8 

		#bitwise of the mask with the input image
		ret,image_mask = cv2.threshold(m,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		output = cv2.bitwise_and(self.image,self.image,mask = image_mask)
		#show the images
		#self.show_image(self.image)
		saida = self.image
		for y in range(image_mask.shape[0]):
			for x in range(image_mask.shape[1]):
				if (image_mask[y,x])== 255:
					saida[y,x] = self.fundo[y,x]
		cv2.imshow("Fundo",self.fundo)
		cv2.imshow("saida",saida)
		#cv2.imshow("Image",self.image)
		#self.show_image(image_mask)
		cv2.imshow("Mask",image_mask)
		#self.show_image(output)
		cv2.imshow("Output",output)

		cv2.waitKey(3)

#================================================================================================================================
	def show_image(self, image):
		#cv2.imshow("Image",image)
		#cv2.waitKey(10)
		cv2.destroyWindow("Image")
#================================================================================================================================

