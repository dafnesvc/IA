"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Detección de Aristas y Segmentación"""
import cv2
import numpy as np


imagen_orig=cv2.imread("Yoda.jpg")
imagen1 = cv2.imread('Yodaver.jpg')
imagen2 = cv2.imread('Yodamor.jpg')
imagen3 = cv2.imread('Yodarojo.jpg')

gris1 = cv2.cvtColor(imagen_orig, cv2.COLOR_BGR2GRAY)#imagenes en escalas de grises 
gris2 = cv2.cvtColor(imagen1, cv2.COLOR_BGR2GRAY)#verde
gris3 = cv2.cvtColor(imagen2, cv2.COLOR_BGR2GRAY)#morado 
gris4 = cv2.cvtColor(imagen3, cv2.COLOR_BGR2GRAY)#rojo

max_value1 = np.amax(gris1)#
max_index1 = np.where(gris1 == max_value1)#Igualamos Max value con max_index

max_value2 = np.amax(gris2)
max_index2 = np.where(gris2 == max_value2)

max_value3 = np.amax(gris3)
max_index3 = np.where(gris3 == max_value3)

max_value4 = np.amax(gris3)
max_index4 = np.where(gris3 == max_value4)

white_patch = imagen_orig[max_index1[0][0], max_index1[1][0]]
white_patch2 = imagen1[max_index2[0][0], max_index2[1][0]]#verde 
white_patch3 = imagen2[max_index3[0][0], max_index3[1][0]]#morado
white_patch4 = imagen3[max_index4[0][0], max_index4[1][0]]#rojo

scale_factors = np.divide(255.0, white_patch)
scale_factors2 = np.divide(255.0, white_patch2)#verde  
scale_factors3 = np.divide(255.0, white_patch3)#morado
scale_factors4 = np.divide(255.0, white_patch4)#rojo 

imagen_corregida = np.clip(imagen_orig * scale_factors, 0, 255).astype(np.uint8)
imagen_corregida2 = np.clip(imagen1 * scale_factors2, 0, 255).astype(np.uint8)
imagen_corregida3 = np.clip(imagen2 * scale_factors3, 0, 255).astype(np.uint8)
imagen_corregida4 = np.clip(imagen3 * scale_factors4, 0, 255).astype(np.uint8)

gamma = 1#Modifica el brillo 
imagen_corregida_gamma1 = np.clip(np.power(imagen_corregida / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)
imagen_corregida_gamma2 = np.clip(np.power(imagen_corregida2 / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)
imagen_corregida_gamma3 = np.clip(np.power(imagen_corregida3 / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)
imagen_corregida_gamma4 = np.clip(np.power(imagen_corregida4 / 255.0, gamma) * 255.0, 0, 255).astype(np.uint8)

imagen_bi2=cv2.cvtColor(imagen_corregida_gamma1, cv2.COLOR_BGR2HSV)
ver_low = np.array([10,50,50], np.uint8)
ver_high = np.array([65,255,255], np.uint8)
mascara_ver = cv2.inRange(imagen_bi2,ver_low,ver_high)


imagen_bi4=cv2.cvtColor(imagen_corregida_gamma2, cv2.COLOR_BGR2HSV)
mascara_ver2 = cv2.inRange(imagen_bi4,ver_low,ver_high)


imagen_bi6=cv2.cvtColor(imagen_corregida_gamma3, cv2.COLOR_BGR2HSV)
mascara_ver3 = cv2.inRange(imagen_bi6,ver_low,ver_high)

imagen_bi8=cv2.cvtColor(imagen_corregida_gamma4, cv2.COLOR_BGR2HSV)
mascara_ver4 = cv2.inRange(imagen_bi8,ver_low,ver_high)

cv2.imshow('Imagen Original', imagen_orig)
cv2.imshow('Imagen corregida Original', imagen_corregida_gamma1)
cv2.imshow("Yoda binary", mascara_ver)



cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagen Color Morado', imagen2)
cv2.imshow('Imagen corregida Morado', imagen_corregida_gamma3)
cv2.imshow("Yoda binary ", mascara_ver3)



cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagen Color VERDE', imagen1)
cv2.imshow('Imagen corregida VERDE', imagen_corregida_gamma2)
cv2.imshow("Yoda binary 3", mascara_ver2)



cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Imagen Color ROJO', imagen3)
cv2.imshow('Imagen corregida ROJO', imagen_corregida_gamma4)
cv2.imshow("Yoda binary 4", mascara_ver4)



cv2.waitKey(0)
cv2.destroyAllWindows()
