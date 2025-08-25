# -*- coding: utf-8 -*-
"""
Created on Sat Aug  2 07:15:06 2025

@author: LORNA
"""
import numpy as np
array= np.matrix([[1,2,3],[4,5,6]])
array2= np.array([[1,2,3],[4,5,6]], float)
array3= np.array([[1,2,3],[4,5,6]], str)

#array 1D
arr1d=np.array([10,20,30,40,50])
print(arr1d[-1]) #imprime el ultimo
print(arr1d[1:4])
a=arr1d[1:4]


arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d.shape #TAMAÑO
arr2d.ndim #DIMENSION

print(arr2d[1,2])
print(arr2d[0,:])
print(arr2d[:,1])
print(arr2d[1:,:2])

a=np.array([[1,2,3,4]])
b=np.array([[5,6,7,8]])
suma=a+b
resta=a-b
producto=a*b
division=b/a
potencia=a**2
print(potencia)

arr=np.array([1,4,9,16])
raiz=np.sqrt(arr)
logaritmo=np.log(arr)
exponencial=np.exp(arr)
seno=np.sin(arr)

arr=np.arange(12)
arr1=np.reshape(arr,(2,6))
arr2=np.reshape(arr,(6,2))
arr3=np.reshape(arr,(3,4))

a=np.array([1,2,3])
b=np.array([4,5,6])

horizontal=np.hstack((a,b))#concatena horizontal
vertical=np.vstack((a,b))#concatena vertical

arr4=np.arange(10)
partes=np.split(arr4,5) #separa el array en las partes dadas

temperaturas=np.random.normal(25,5,168) #media=25,desv=5,
print(np.mean(temperaturas)) #numero mas bajo
print(np.max(temperaturas)) #numero mas alto
print(np.std(temperaturas)) #desviacion, cuanto se desvian de la media

t=np.linspace(0,2*np.pi,1000)
y=np.sin(5*t)
import matplotlib.pyplot as plt
plt.plot(t,y, c="pink")
plt.xlabel("Valores en X")
plt.ylabel("Funcion en Y")
plt.title("Funcion sin(5t")
plt.grid(True)
plt.savefig("Figura,png") #descarga la figura en la misma rua de donde estan los proyectos


##Una matriz identidad
import numpy as np
def matriz_identidad(n):
    mat=np.identity(n)
    return mat

#matriz de ceros
def matriz_ceros(a,b):
    return np.zeros((a,b))

#matriz random
def matriz_random1(a,b):
    return np.random.rand(a,b)    

def matriz_random1(a,b):
    return np.random.randint(3,11, (a,b))

matriza=matriz_identidad(8)
matrizb=matriz_ceros(4,2)
matrizc=matriz_random1(5,2)

