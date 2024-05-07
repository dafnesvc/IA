"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Etiquetados de Líneas"""

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
 
img = cv.imread('Messi.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,100,200)
 
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


plt.show()
