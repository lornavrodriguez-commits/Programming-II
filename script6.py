# -*- coding: utf-8 -*-
"""
Created on Wed Aug  6 10:20:32 2025

@author: LORNA
"""

class Animal:
    #Atributos
    tipo_animal=""
    color=""
    raza=""
    collar= False
#metodos
def sonido ():
    return sonido 
def corre ():
    return False
def camina():
    return False
def vuela ():
    return False
def nada ():
    return True

#objeto
perro= Animal()
gato= Animal()
gallo= Animal ()
culebra= Animal()
pez=Animal()

perro.tipo_animal="Canino"
perro.color="Cafe"
perro.raza="Retriever"
perro.collar=True     

print(f"Animal:{perro.tipo_animal}")
print(f"Color:{perro.color}")
print(f"Raza:{perro.raza}")
print(f"Tiene collar:{perro.collar}")