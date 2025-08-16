# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 09:55:29 2025

@author: centro.potencias
"""

##funciones: modularizar el codigo

def suma (num1,num2):
    return num1+num2


def resta(num1, num2):
    return num1 - num2


def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: división por cero"


def division_entera(num1, num2):
    if num2 != 0:
        return num1 // num2
    else:
        return "Error: división por cero"


def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num1):
    if num1 >= 0:
        return num1 ** 0.5
    else:
        return "Error: no se puede calcular la raíz cuadrada de un número negativo"


def raiz_cubica(num2):
    # Permite raíz cúbica de negativos
    if num2 >= 0:
        return num2 ** (1/3)
    else:
        return -(-num2) ** (1/3)


###

def saludo():
    print("Hola")

def saludo_pred(nombre):
    print(f"Hola {nombre}, sea bienvenido al curso")

