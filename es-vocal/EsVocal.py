import sys

"""
Archivo: EsVocal
Descripción: Programa que captura un carácter e indica si es una vocal: a, e, i, o, u, A, E, I, O, U, á, é, í, ó, ú, Á, É, Í, Ó, Ú, ü, Ü
Autor: Adrian Alvarez
Fecha: 14/OCT/26
"""

print("Programa que captura un carácter e indica si es una vocal.")

caracterIngresado = input("Ingrese un carácter: ")

if len(caracterIngresado) == 1:
    match caracterIngresado.lower():
        case "a" | "e" | "i" | "o" | "u" | "á" | "é" | "í" | "ó" | "ú" | "ü":
            print("El carácter ingresado es una vocal!")
        case _ :
            print("El carácter ingresado NO es una vocal!")
else:
    print("Error: Debe ser un solo carácter...", file = sys.stderr)