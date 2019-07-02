import pyscreenshot as ImageGrab
im = ImageGrab.grab()
im.save('c:\_install\tobot\dev_arduino\screenshot.png')
im.show()
import cv2
import numpy as np
image = cv2.imread("image.png") # or full path to image

print(image.size)
print(image.shape)    
print (image[0,0])
ser.write(image[0,0])
