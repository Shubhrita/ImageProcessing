# installing the dependency libraries through command line

#pip install open-cv python

# importing libaries

import numpy as np
import cv2
import argparse
# defining functions to be used

def transform(input_image,points):

	# Creating new variable to hold the coordinates

	coordinates=np.zeros((4,2),dtype='float32')
	for i in range(len(points)):
		coordinates[i] = points[i]

	# assigning names to coordinates

	# A is topleft point
	# B is topright point
	# C is bottomright point
	# D is bottomleft point
	# This order should be maintained through out the program as well as while giving input through command line

	(A,B,C,D) = coordinates

	# calculating width and height of the distorted image

	# width of distorted image will be the maximum distance between the topleft and topright x-ccordinates or bottomleft and bottomright x-coordinates

	width1 = np.sqrt(((C[0] - D[0]) ** 2) + ((C[1] - D[1]) ** 2))
	width2 = np.sqrt(((B[0] - A[0]) ** 2) + ((B[1] - A[1]) ** 2))
	width = max(int(width1), int(width2))
 
	# height of the distorted image, will be the maximum distance between the topright and bottomright y-coordinates or the topleft and bottomleft y-coordinates
	height1 = np.sqrt(((B[0] - C[0]) ** 2) + ((B[1] - C[1]) ** 2))
	height2 = np.sqrt(((A[0] - D[0]) ** 2) + ((A[1] - D[1]) ** 2))
	height = max(int(height1), int(height2))

	new_coordinates = np.array([
		[0, 0],
		[width - 1, 0],
		[width - 1, height - 1],
		[0, height - 1]], dtype = "float32")
 
	# computing the perspective transform matrix and then applying it

	M = cv2.getPerspectiveTransform(coordinates, new_coordinates)
	warped = cv2.warpPerspective(input_image, M, (width, height))
 
	# return the warped image
	return warped

# main function

# construct the argument parse and parse the arguments
a = argparse.ArgumentParser()
a.add_argument("-i", "--input_image", help = "path to the image file")
a.add_argument("-c", "--coordinates",
	help = "comma separated list of source points")
args = vars(a.parse_args())
 
# reading the input image and extracting the coordinates

image = cv2.imread(args["input_image"])
pts = np.array(eval(args["coordinates"]), dtype = "float32")
 
distorted = transform(image, pts)
 
# displaying original and distorted image

cv2.imshow("Original Image", image)
cv2.imshow("Distorted Image", distorted)
cv2.waitKey(0)

# calling the above function from commandline

# python open_cv_assignment.py --input_image C:/GreedyGame/sample.jpg --coordinates "[(100,200),(300,200),(100,100),(300,100)]"












