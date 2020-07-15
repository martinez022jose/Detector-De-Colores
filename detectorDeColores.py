import cv2
import numpy as np

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

#Generamos mascaraTriple(ejemplo particular)

maskAmarrillo = cv2.inRange(imagenHSV,amarilloBajo,amarilloAlto)
maskRojo1 = cv2.inRange(imagenHSV,rojoBajo1,rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV,rojoBajo2,rojoBajo2)
maskRojoTotal = cv2.add(maskRojo1,maskRojo2)
maskVerde = cv2.inRange(imagenHSV,verdeBajo,verdeAlto)

maskRojoAmarillo = cv2.add(maskAmarrillo,maskRojoTotal)
maskConjunto = cv2.add(maskVerde,maskRojoAmarillo)

#Mostramos mascara diferenciada 

maskConjuntoAMostrar = cv2.bitwise_and(imagen,imagen,mask =maskConjunto)

#Imprimimos colores

cv2.imshow("Original", imagen)
cv2.imshow("ConjuntoTriple", maskConjuntoAMostrar)

print("\nPulsa cualquier tecla para cerrar las ventanas\n")
cv2.waitKey(0)
cv2.destroyAllWindows()