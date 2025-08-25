# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 09:13:20 2025

@author: LORNA
"""
class Automovil:
    # Atributos - Inicializarlos - Metodo Constructor
    # Encapsular -> atributos, metodos __variables, __metodos()
    def __init__(self):
        self.__largoChasis = 2.50
        self.__anchoChasis = 1.20
        self.__ruedas = 4
        self.__enMarcha = False
        print("Inicializada las variables")
   
    # Metodos
    def arrancar(self, arranca):
        self.__enMarcha = arranca
       
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()
       
        if(self.__enMarcha)and(chequeo):
            return "El automóvil se encuentra en movimiento"
        elif (self.__enMarcha) and (chequeo == False):
            return "Algo salio mal. EL VEHICULO NO PUEDE ARRANCAR"    
        else:
            return "El automovil esta detenido"
       
    def estado(self):
        print(f"El automovil tiene un largo de chasis {self.__largoChasis} m, con un ancho de chasis {self.__anchoChasis} m, y tiene {self.__ruedas} ruedas.")
   
    # chequear los testigos
    def __chequeoInterno(self):
        print("Realizando chequeo")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.temperatura = "ok"
        self.puertas = "abiertas"
        if (self.gasolina == "ok") and (self.aceite == "ok") and (self.temperatura == "ok") and (self.puertas == "cerradas"):
            return True
        else:
            return False

# %% - Instanciando Objetos
# Automovil 1
print("Creacion de objeto 1")
automovil1 = Automovil()
print(automovil1.arrancar(False))
automovil1.estado()

print("--------------- Objeto 2 ----------")
# Automovil 1
mustang = Automovil()
print(mustang.arrancar(True))
mustang.estado()

#############   
import random

class Estudiante:
    def __init__(self):
        self.nombre = ""
        self.edad = None
        self.identificacion = None
        self.calificacion = None
        print("Estudiante Creado")

    def datos(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion
        self.edad = random.randint(18, 30)  # Edad aleatoria

    def calificacion_final(self, notas):
        total = sum(notas)
        self.calificacion = total / len(notas)

    def resumen(self):
        estado = "APROBÓ" if self.calificacion >= 3 else "NO APROBÓ"
        return f"Nombre: {self.nombre}, Edad: {self.edad}, ID: {self.identificacion}, Promedio: {self.calificacion:.2f} -> {estado}"


# Crear lista de estudiantes
estudiantes = []

# Estudiante 1
est1 = Estudiante()
est1.datos("Wilfredo", 1087)
est1.calificacion_final([4.5, 4.0, 4.8, 4.7, 5.0])
estudiantes.append(est1)

# Estudiante 2
est2 = Estudiante()
est2.datos("Juan Felipe", 4567)
est2.calificacion_final([4.2, 4.4, 4.1, 4.8, 4.6])
estudiantes.append(est2)

# Estudiante 3
est3 = Estudiante()
est3.datos("Lorna", 7890)
est3.calificacion_final([4.3, 4.7, 4.9, 4.8, 5.0])
estudiantes.append(est3)

# Estudiante 4
est4 = Estudiante()
est4.datos("Nicolas", 2345)
est4.calificacion_final([4.0, 4.2, 4.1, 4.3, 4.5])
estudiantes.append(est4)

# Estudiante 5
est5 = Estudiante()
est5.datos("Roger", 6789)
est5.calificacion_final([4.6, 4.7, 4.5, 4.8, 4.9])
estudiantes.append(est5)




# Consulta por nombre
nombre_buscar = input("\nIngresa el nombre del estudiante para ver su información: ")

encontrado = False
for est in estudiantes:
    if est.nombre.lower() == nombre_buscar.lower():
        print("\n" + est.resumen())
        encontrado = True
        break

if not encontrado:
    print("\nEstudiante no encontrado.")
