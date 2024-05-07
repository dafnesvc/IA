"""Dafne Sarahi Villanueva Ceja 21310176
Probabilidad (Incertidumbre)---> Percepción---> Texturas y Sombras"""
import cv2
import numpy as np

imagen=cv2.imread("Yoda.jpg")
m,c,n=imagen.shape #array donde se guardan altura ancho y codigo rgb

cv2.imshow("Original", imagen)# imshow nombre de ventana y toma el recurso en este caso la imagen jpg.
imagencroma=imagen.copy() #crea una copia para que la original no se vea afectada
imagencroma=imagencroma.astype(np.float32) #astype dice los bits que tiene la imagen 
imagen=imagen.astype(np.float32)# np significa que es un array
for x in range(m):
    for y in range(c):
        imagencroma[x,y,0]=imagen[x,y,0]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        imagencroma[x,y,1]=imagen[x,y,1]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])    
        imagencroma[x,y,2]=imagen[x,y,2]/(imagen[x,y,0]+imagen[x,y,1]+imagen[x,y,2])
        
imagencroma=imagencroma*255 
imagencroma=imagencroma.astype(np.uint8)# con unit8 se le baja la resolución a 8 bits
   
cv2.imshow("imagen cromatica 1", imagencroma)#para mostrar la imagen cromatica

imagen_bi=cv2.cvtColor(imagencroma, cv2.COLOR_BGR2HSV)
a_low = np.array([30,55,55], np.uint8)
a_high = np.array([240,255,255], np.uint8)
mascara=cv2.inRange(imagen_bi,a_low,a_high)


cv2.imshow("Imagen binaria",mascara)
cv2.waitKey(0)
cv2.destroyAllWindows()


imagenosc1=imagen*0.5
imagenosc1=imagenosc1.astype(np.uint8)

cv2.imshow("oscurecido1", imagenosc1)
imagenc1=imagenosc1.copy()
imagenc1=imagenc1.astype(np.float32)
imagenosc1=imagenosc1.astype(np.float32)

for x in range(m):
    for y in range(c):

        imagenc1[x,y,0]=imagenosc1[x,y,0]/(imagenosc1[x,y,0]+imagenosc1[x,y,1]+imagenosc1[x,y,2])
        imagenc1[x,y,1]=imagenosc1[x,y,1]/(imagenosc1[x,y,0]+imagenosc1[x,y,1]+imagenosc1[x,y,2])
        imagenc1[x,y,2]=imagenosc1[x,y,2]/(imagenosc1[x,y,0]+imagenosc1[x,y,1]+imagenosc1[x,y,2])


imagenc1=imagenc1*255
imagenc1=imagenc1.astype(np.uint8)

cv2.imshow("imagen cromatica 2",imagenc1)


imagen_bi2=cv2.cvtColor(imagenc1, cv2.COLOR_BGR2HSV)
a_low = np.array([30,55,55], np.uint8)
a_high = np.array([240,255,255], np.uint8)
mascara2=cv2.inRange(imagen_bi2,a_low,a_high)


cv2.imshow("Imagen binaria2",mascara2)
cv2.waitKey(0)
cv2.destroyAllWindows()



imagenosc3=imagen*0.2
imagenosc3=imagenosc3.astype(np.uint8)

cv2.imshow("oscurecido2", imagenosc3)
imagenc3=imagenosc3.copy()
imagenc3=imagenc3.astype(np.float32)
imagenosc3=imagenosc3.astype(np.float32)

for x in range(m):
    for y in range(c):

        imagenc3[x,y,0]=imagenosc3[x,y,0]/(imagenosc3[x,y,0]+imagenosc3[x,y,1]+imagenosc3[x,y,2])
        imagenc3[x,y,1]=imagenosc3[x,y,1]/(imagenosc3[x,y,0]+imagenosc3[x,y,1]+imagenosc3[x,y,2])
        imagenc3[x,y,2]=imagenosc3[x,y,2]/(imagenosc3[x,y,0]+imagenosc3[x,y,1]+imagenosc3[x,y,2])


imagenc3=imagenc3*255
imagenc3=imagenc3.astype(np.uint8)

cv2.imshow("imagen cromatica 3",imagenc3)


imagen_bi3=cv2.cvtColor(imagenc1, cv2.COLOR_BGR2HSV)
a_low = np.array([30,55,55], np.uint8)
a_high = np.array([240,255,255], np.uint8)
mascara3=cv2.inRange(imagen_bi3,a_low,a_high)

cv2.imwrite("Imagen Binarizada 3.jpg",mascara3)
cv2.imshow("Imagen binaria3",mascara3)
cv2.waitKey(0)
cv2.destroyAllWindows()