import cv2
import numpy as np
from matplotlib import pyplot as plt

#This is the bgr value of land that we are going to change to a brighter colour for high contrast
bgrvalue_land=[ 34, 150,  31] 
img_location=input("Enter the path to the image:")
image = cv2.imread(img_location)

#To get an image that clearly depicts land and sea with two contrasting colours
Change_colour=[0,255,255]
mask = cv2.inRange(image, np.array(bgrvalue_land), np.array(bgrvalue_land))
image[mask == 255] = Change_colour
cv2.imwrite("land&seacontrasted.png",image)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.axis("off")
plt.show()
