# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 07:30:29 2025

@author: LORNA
"""

##Ejercicio Clase Financiera
class Banco:
    def __init__(self, Movimientos=None):
        self.Movimientos = Movimientos or {}

    def Promedio(self, Cliente):
        if Cliente in self.Movimientos and self.Movimientos[Cliente]:
            return sum(self.Movimientos[Cliente]) / len(self.Movimientos[Cliente])
        return None

    def Riesgo(self, Cliente):
        prom = self.Promedio(Cliente)
        if prom is None:
            return "Cliente no encontrado"
        if prom < 0:
            return "Alto riesgo"
        elif prom < 10_000_000:
            return "Riesgo medio"
        else:
            return "Riesgo bajo"


def main():
    Movimientos = {}
    n = int(input("¿Cuántos clientes desea registrar? "))

    for i in range(1, n + 1):
        Cliente = input(f"\nIngrese el nombre del cliente {i}: ")
        Movimientos[Cliente] = []

        m = int(input(f"¿Cuántos movimientos tiene {Cliente}? "))
        for j in range(1, m + 1):
            Valor = float(input(f"   Movimiento {j}: "))
            Movimientos[Cliente].append(Valor)

    BancoInstancia = Banco(Movimientos)

    print("\n--- Resultados ---")
    for Cliente in Movimientos:
        PromedioCliente = BancoInstancia.Promedio(Cliente)
        print(f"\nCliente: {Cliente}")
        print(f"Promedio: {PromedioCliente:.2f}" if PromedioCliente is not None else "Promedio: N/A")
        print(f"Categoría de riesgo: {BancoInstancia.Riesgo(Cliente)}")


if __name__ == "__main__":
    main()
