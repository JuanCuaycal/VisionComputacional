# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 16:11:59 2018

@author: 
    Chaquinga Joselyn
    Cuaycal Juan 
    Dominguez Luis
    Sarmiento Michael
    Oña Martín
"""


#Importamos los módulos a utilizar
import cuadrados_rectangulos as cr  #Módulo cuadrados_rectangulos.py
import triangulos as t #Módulo triangulos.py
import circulos as c #Módulo circulos.py


print("")
print("UNIVERSIDAD CENTRAL DEL ECUADOR")
print("INGENIERÍA CIENCIAS FÍSICAS Y MATEMÁTICA")
print("INGENIERÍA EN COMPUTACIÓN GRÁFICA")
print("VISIÓN COMPUTACIONAL")
print("")
print("""INTEGRANTES:
*JOSELYN CHAQUINGA
*JUAN GUAYCAL
*LUIS DOMINGUEZ
*MARTIN OÑA
*MICHAEL SARMIENTO""")
print("")
    
while(True):
    print("""¿QUÉ FIGURA QUIERES INDENTIFICAR ?, Escribe una opción
    1) 4 VERTICES
    2) 3 VERTICES
    3) CIRCULOS
    4) SALIR  \n\t"""+"""
    Digite la Opción:""")
  
    opcion = input()
    if opcion == '1':
       cr.cuadrados_rectangulosf()
       print("Se han procesado las imagenes con 4 Vertices")
       print("")
        
    elif opcion == '2':
        
        t.triangulosf()
        print("Se han procesado las imagenes con 3 Vertices")
        print("")
        
    elif opcion == '3':
        
        c.circulosf()
        print("Se han procesado las imagenes que contienen circulos")
        print("")
        
    elif opcion =='4':
        
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    
    else:
        print("Comando desconocido, vuelve a intentarlo")