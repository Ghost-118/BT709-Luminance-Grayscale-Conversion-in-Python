# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:59:43 2024

@author: jose ochoa
"""

import cv2 

# Lista de archivos a procesar
imagenes = ["img1", "img2", "img3"]

# Pesos para la conversión a escala de grises
wr = 0.2125
wg = 0.7154
wb = 0.072

for ruta in imagenes:
    img = cv2.imread(f"{ruta}.jpg")
    
    # Separación de canales RGB (OpenCV usa BGR)
    r = img[:,:,2]
    g = img[:,:,1]
    b = img[:,:,0]
   
    # Promedio ponderado y conversión a enteros
    n_img = (wr*r + wg*g + wb*b)/3
    n_img = n_img.astype(int)
    
    # Guardar imagen resultante
    cv2.imwrite(f"{ruta}_E10.jpg", n_img) 
