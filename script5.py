# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 07:18:01 2025

@author: LORNA
"""

import numpy as np
import math

#Pida al usuario un número y calcule su raíz cuadrada.
#Maneje ValueError si ingresa un texto.
#Maneje una excepción personalizada NumeroNegativoError si el número es negativo.
#Use finally para mostrar un mensaje de finalización.


def calcular_raiz():
    try:
        num = float(input("Ingresa un número: "))  

        if num < 0:
            print("Error: No se puede calcular la raíz de un número negativo.")
        else:
            resultado = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es: {resultado}")

    except ValueError:
        print("Error: Ingrese necesariamente un número.")

    finally:
        print("Fin del programa")

calcular_raiz()


##Biblioteca TIME

import time
print("Inicio")
time.sleep(2)
print("Fin despues de dos segundos") #DURA DOS SEGUNDOS


inicio=time.time()
time.sleep(3)
fin=time.time()
print(f"Tiempo transcurrido: {fin - inicio} segundos ") #Cuanto duro en ejecutarse


tiempo_actual = time.localtime()
print("Año:", tiempo_actual.tm_year)
print("Hora actual:", f"{tiempo_actual.tm_hour}:{tiempo_actual.tm_min}") #


formato = "%d/%m/%Y %H:%M:%S"
fecha_legible = time.strftime(formato, time.localtime())
print("Fecha y hora:", fecha_legible) #fecha mas especifica


##RANDOM
import random

dado = random.randint(1, 6)
print("Lanzamiento de dado:", dado) #NUMERO RANDOM ENTRE 1 Y 6


colores = ["rojo", "verde", "azul"]
color_aleatorio = random.choice(colores)
print("Color seleccionado:", color_aleatorio) #SELECCIONA ALTEATORIO DE UNA LISTA


cartas = ["As", "2", "3", "Reina"]
random.shuffle(cartas)
print("Cartas mezcladas:", cartas)














