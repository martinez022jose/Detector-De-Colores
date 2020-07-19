import cv2
import numpy as np

def mostrarColor(mascaraADibujar):
    kernel = np.ones((10,10))
    mascara = cv2.morphologyEx(mascaraADibujar,cv2.MORPH_OPEN,kernel)
    mascara = cv2.morphologyEx(mascaraADibujar,cv2.MORPH_CLOSE,kernel)

    color = cv2.bitwise_and(imagen,imagen,mask = mascara)

    cv2.imshow("Original", imagen)
    cv2.imshow("Color", color)

    print("\nPulsa cualquier tecla para generar un color\n")
    cv2.waitKey(0)

#Leer imagen 
imagen = cv2.imread("pruebaColores.jpg")

#Generar HSV
imagenHSV = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

#Generamos rangos a analizar
azulBajo = np.array([100,50,50])
azulAlto = np.array([125, 255, 255])

rojoBajo1 = np.array([0, 100, 20])
rojoAlto1 = np.array([4, 255, 255])
rojoBajo2 = np.array([175, 100, 20])
rojoAlto2 = np.array([180, 255, 255])

amarilloBajo = np.array([25,100,20])
amarilloAlto = np.array([35,255,255])

verdeBajo = np.array([40,50,20])
verdeAlto = np.array([65,255,255])

#Generamos mascaras

maskAmarrillo = cv2.inRange(imagenHSV,amarilloBajo,amarilloAlto)

maskRojo1 = cv2.inRange(imagenHSV,rojoBajo1,rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV,rojoBajo2,rojoBajo2)
maskRojoTotal = cv2.add(maskRojo1,maskRojo2)

maskVerde = cv2.inRange(imagenHSV,verdeBajo,verdeAlto)

maskAzul = cv2.inRange(imagenHSV,azulBajo,azulAlto)

#Generamos mascara total

maskRojoAmarillo = cv2.add(maskAmarrillo,maskRojoTotal)
maskRojoAmarilloAzul = cv2.add(maskRojoAmarillo,maskAzul)
maskConjunto = cv2.add(maskVerde,maskRojoAmarilloAzul)

mostrarColor(maskVerde)
mostrarColor(maskRojoTotal)
mostrarColor(maskAmarrillo)
mostrarColor(maskAzul)
mostrarColor(maskConjunto)

cv2.destroyAllWindows()