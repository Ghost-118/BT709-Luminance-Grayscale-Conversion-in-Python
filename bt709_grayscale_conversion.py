# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:59:43 2024

@author: jose ochoa
"""

import cv2 

imagenes = ["img1", "img2", "img3"]

wr = 0.2125
wg = 0.7154
wb = 0.072

for ruta in imagenes:
    img = cv2.imread(f"{ruta}.jpg")
    
    r = img[:,:,2]
    g = img[:,:,1]
    b = img[:,:,0]
   
    n_img = (wr*r + wg*g + wb*b)/3
    n_img = n_img.astype(int)
    
    cv2.imwrite(f"{ruta}_E10.jpg", n_img)   