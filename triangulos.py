#Permite la detección
#de triángulos mediante el procesamiento de contornos y áreas
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
  #EXTRAE LOS CONTORNOS DE TODA LA IMAGEN 
def get_all_contours(img): 
    #Transformamos a escala de grises
    ref_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Aplicamos el umbral
    ret, thresh = cv2.threshold(ref_gray, 127, 255, 0)
    #Encontramos contornos en una imagen binaria
    im2, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE )
    return contours

def triangulosf():
    #Abrimos el Dataset
    
    with open('../data/nombres.csv', newline='') as File:   #Abre la ruta del archivo
        reader= csv.reader(File)
        for row in reader:
            imagen = cv2.imread("../dataset/"+row[0]) 
             #OBTIENE LOS CONTORNOS
            contours = get_all_contours(imagen) 
            #CALCULA LOS FACTORES DE SOLIDEZ DE TOODS LOS CONTORNOS.
            areas = [cv2.contourArea(c) for c in contours]
            i = 0
            for extension in areas:
                if extension > 600:
                    actual = contours[i]
                    #Se aproxima la curva poligonal y se describe la forma
                    approx = cv2.approxPolyDP(actual,0.05*cv2.arcLength(actual,True),True)
                    if len(approx)==3:
                        #Se procede a dibujar los contornos
                        cv2.drawContours(imagen,[actual],0,(0,0,0),2)
                    i = i+1
                    #SE GUARDA EL RESULTADO
                   #Se procede guardando la imagen en un archivo específico    
            cv2.imwrite("../salidaTriangulos/"+row[0]+".jpg",imagen)
