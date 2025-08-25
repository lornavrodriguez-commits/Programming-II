# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 07:32:40 2025

@author: LORNA
"""

# %% Biblioteca numpy

import numpy as np ##vectoriza info
import math ##Guarda variables
print(np.pi)
print(math.pi)
print(np.e)

vector1= [5,6,8]
vector2=np.array([5,6,8])
vector3= np.array([[5,7,8,4],[3,2,1,0]])

print(f"dimension {vector3.ndim}")#dimension
print(f"dimension {vector3.shape}")#longitud

print(vector3)

iteracion=0
for fila in vector3:
    iteracion +=1
    print(f"{iteracion}:{fila}") ##itera por cada fila, pasa x cada fila y la da

for fila in vector3:
    for elemento in fila:
        print(elemento) #imprime cada elemento d la fila, uno por uno
        
for fila in vector3:
    for elemento in fila:
        print(elemento,end="")
        print() #imprime cada elemento en fila xq esta el end, sino lo imprimiria igual

vector4= np.array([[5,7,8.3,4],[3,2,1,0]])
for fila in vector4:
    for elemento in fila:
        print(elemento, end=" ")
    print() #convierte todos los elementos a lo mismo, x eso el .0, x el 8.3

type(vector3[1][2])
type(vector4[1][2]) #que tipo de datos tiene

vector5=np.zeros((3,3))
vector6=np.ones((3,3))
vector7=np.eye(5)
vector8=np.full((3,2),5)
vector9=np.full((5,), 7)
vector10=np.random.rand(4,3)
vector11= np.random.randint(0, 11, (8, 3))
vector12=np.identity(5)

vector13=np.arange(1,11,2)#del 1 al 11 en pasos de 2, sin incluir el 11
vector14=np.linspace(1,11,3)#del 1 al 11, tres valores


