
#Permite la detección y censura
#de cuadrados y rectángulos mediante el procesamiento de contornos y áreas
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
 
def cuadrados_rectangulosf():
    
  #ABRE EL DATASET (ARCHIVO . CSV)
    with open('../data/nombres.csv', newline='') as File:  #Abre la ruta del archivo
        #Leemos el achivo csv
        reader= csv.reader(File)
        for row in reader:
            #leemos las imagenes del dataset
            img = cv2.imread("../dataset/"+row[0])  #lee el archivo
            img_orig = np.copy(img) 

            #OBTIENE LOS CONTORNOS
            input_contours = get_all_contours(img) 
            contour_img = img.copy()
            cv2.drawContours(contour_img, input_contours, -1, color=(0,0,0), thickness=3) 
            

            solidity_values = [] 
            #CALCULA LOS FACTORES DE SOLIDEZ DE TOODOS LOS CONTORNOS.
            for contour in input_contours: 
                epsilon = 0.00001 * cv2.arcLength(contour, True) 
                #Se aproxima la curva poligonal y se describe la forma
                approx=cv2.approxPolyDP(contour, epsilon, True)
                if len(approx) is 4:  #Número de vertices a detectar dentro de la imágen
                    #Se procede a dibujar los contornos
                    cv2.drawContours(img, approx, -1, (0,0,0), 3)
                    solidity_values.append(contour)

           

            output_contours = [] 

            for i in solidity_values:
                output_contours.append(i)

            cv2.drawContours(img, output_contours, -1, (0,0,0), 3) 
           

             # IDENTIFICA LA FIGURA GEOMETRICA
            for contour in output_contours: 
                rect = cv2.minAreaRect(contour) 
                box = cv2.boxPoints(rect) 
                box = np.int0(box) 
                cv2.drawContours(img_orig,[box],0, (0,0,0), -1) 

            #SE GUARDA EL RESULTADO
        
            cv2.imwrite("../salidaCuadradosyRectangulos/"+row[0]+".jpg",img_orig)

          
