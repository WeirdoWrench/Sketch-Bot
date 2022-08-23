import cv2  
import tkinter as tk
from tkinter import filedialog

root = tk. Tk()
root. withdraw()

file = filedialog. askdirectory()
image_name = input("Enter the image name(with extension):")

img = cv2.imread( file + '/' + image_name )

gray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
invert_gray = 255 - gray

def new_func(invert_gray):
    blur = cv2.GaussianBlur(invert_gray, (25, 25),0,0 )
    return blur

blur = new_func(invert_gray)
invert_blur = 255 - blur

pencil_sketch = cv2.divide(gray, invert_blur, scale = 250.0)

cv2.imwrite('Sketch_' + image_name, pencil_sketch)
cv2.imshow('Original',img)
cv2.imshow('Sketch', pencil_sketch)
cv2.waitKey(0)