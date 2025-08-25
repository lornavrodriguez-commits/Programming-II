# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 19:28:58 2025

@author: LORNA
"""

#PARCIAL 1: LORNA VANESSA RODRIGEZ CUESTA
import random

# ==========================
class IndiceInvalidoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class MatrizCalificaciones:
    def __init__(self):
        self.__matriz = []  # atributo privado
    
    def ingresar_valores(self, n, m):
        """Llena la matriz con valores aleatorios entre 0.0 y 5.0"""
        self.__matriz = [[round(random.uniform(0.0, 5.0), 2) for _ in range(m)] for _ in range(n)]
    
    def mostrar(self):
        """Imprime la matriz de forma tabular"""
        print("\n=== MATRIZ DE CALIFICACIONES ===")
        for fila in self.__matriz:
            for valor in fila:
                print(f"{valor:<6}", end=" ")
            print()
    
    def promedio_estudiante(self, i):
        """Devuelve el promedio del estudiante i"""
        if i < 0 or i >= len(self.__matriz):
            raise IndiceInvalidoError(f"Índice {i} fuera de rango. Debe estar entre 0 y {len(self.__matriz)-1}")
        return sum(self.__matriz[i]) / len(self.__matriz[i])
    
    def promedio_general(self):
        """Devuelve el promedio de todas las notas"""
        total = sum(sum(fila) for fila in self.__matriz)
        cantidad = sum(len(fila) for fila in self.__matriz)
        return total / cantidad
    
    def nota_maxima(self):
        """Devuelve la nota más alta y su posición (estudiante, evaluación)"""
        max_nota = -1
        pos = (0, 0)
        for i, fila in enumerate(self.__matriz):
            for j, valor in enumerate(fila):
                if valor > max_nota:
                    max_nota = valor
                    pos = (i, j)
        return max_nota, pos

# Programa:
print("=== PARCIAL: MATRIZ DE CALIFICACIONES ===")

# Crear objeto
matriz = MatrizCalificaciones()

# Ingresar valores aleatorios
n = 4  # número de estudiantes
m = 3  # número de evaluaciones
matriz.ingresar_valores(n, m)

matriz.mostrar()

try:
    indice = int(input(f"\nIngrese el número del estudiante (0 a {n-1}): "))
    promedio = matriz.promedio_estudiante(indice)
    print(f"Promedio del estudiante {indice}: {promedio:.2f}")
except IndiceInvalidoError as e:
    print("Error:", e)
except ValueError:
    print("Debe ingresar un número entero válido.")

# Mostrar promedio general
print(f"\nPromedio general de todas las notas: {matriz.promedio_general():.2f}")

# Mostrar nota máxima y su ubicación
nota, (i, j) = matriz.nota_maxima()
print(f"\nNota máxima: {nota} (Estudiante {i}, Evaluación {j})")
