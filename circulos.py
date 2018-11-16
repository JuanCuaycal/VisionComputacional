
#Permite la detección
#de círculos mediante la función de la transformada circular de Houg
#de un dataset de 105 figuras geométricas básicas
#el cual fue elaborado por los integrantes del grupo
"""
@author: 
    Chaquinga Joselyn
    Cuaycal Juan 
    Dominguez Luis
    Sarmiento Michael
    Oña Martín
"""
import cv2
import numpy as np
import csv

def circulosf():
    with open('../data/nombres.csv', newline='') as File:   #Abre la ruta del archivo y lo lee 
        reader= csv.reader(File)
        for row in reader:
           
            img = cv2.imread("../dataset/"+row[0]) 
            img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # ESCALA DE GRISES 
            
            #Copia de la imagen original 
            copia=img.copy()
          
             #Utilizamos TRY / EXCEPT para actuar si dentro de la imagen no existe un circulo            
            try:
                
                #Método de Hough para detectar circulos dentro de la imagen 
                circulos = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,2,50,
                                            param1=90,param2=50,minRadius=10,maxRadius=90)
                
                #aplicamos el rednodneo, eto se debe a la represetnacion de una matriz 
                circulos = np.uint16(np.around(circulos))
                #Aquí vamos a recorrer los circulos detectados  en una pisicon encuntra radio centro,etc
                #Para cada Círculo
                #Va e cero hasta que termine
                for ciruloActual in circulos [0,:]:
                    #Extraemos el centro
                    centroX=ciruloActual[0]
                    centroY=ciruloActual[1]
                    #el radio tambien tiene el área
                    radio=ciruloActual[2]
                    #dibujamos(que matriz)
                    cv2.circle(copia,(centroX,centroY),radio,(0,255,255),2)

                cv2.imwrite("../salidaCirculos/"+row[0]+".jpg",copia)                  
            except:
                cv2.imwrite("../salidaCirculos/"+row[0]+".jpg",img)

