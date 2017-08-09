# installing the dependency libraries through command line

#pip install open-cv python
#pip install pandas

# importing libaries

import cv2
import argparse

# defining function to zoom image using pivot point and scale given as input

def zoom_image(input_image,x,y,scale):

	# reading and visualizing the input image
	output_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
	cv2.imshow('Original Image',output_image)


	# locating all the possible connected neighbouring pixels
	lx=x-scale
	ly=y-scale

	# zooming using the pivot point by making all the connected pixel locations' intensity value equal to the pivot-point pixel intensity value
	
	for i in range(1,scale):
		for j in range(1,scale):
			output_image[lx+i][ly+j]=output_image[x][y]

	# displaying the output image

	cv2.imshow('Zoomed Image',output_image)
	cv2.waitKey()


# main function

# construct the argument parse and parse the arguments
a = argparse.ArgumentParser()
 
# path of input image
a.add_argument("-i", "--input_image", help = "path to the image file")

# coordinates of pivot point given as x,y
a.add_argument("-c", "--coordinates",
	help = "comma separated list of source points")

# scale value
a.add_argument("-int", "--scale", help = "scale to which image is to be zoomed",default=0)
args = vars(a.parse_args())
 
# reading the input image and extracting the coordinates and scale

image = cv2.imread(args["input_image"])
pivot_point=eval(args["coordinates"])
x_value=0
y_value=0
x_value,y_value=pivot_point        # x and y coordinates of pivot point
scale_value=args["scale"]    # determining scale of zoom
zoom_image(image,int(x_value),int(y_value),int(scale_value))


# calling the above function from commandline

# python open_cv_assignment_2.py --input_image C:/GreedyGame/sample.jpg --coordinates "(100,200)" --scale 50

