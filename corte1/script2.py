# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 10:31:48 2025

@author: centro.potencias
"""

import script1 as s1

s1.saludo()
nombre = input("Ingrese su nombre: ")
s1.saludo_pred(nombre)

num1 = int(input("Ingrese su primer número: "))
num2 = int(input("Ingrese su segundo número: "))

print("La suma es:", s1.suma(num1, num2))
print("La potencia es:", s1.potencia(num1, num2))
print("La raíz cuadrada del primer número es:", s1.raiz_cuadrada(num1))

