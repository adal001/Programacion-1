"""
Archivo: ListaNúmeros.py
Descripción: Programa que captura n números, los almacena en una lista y construye una segunda lista con los elementos de la lista original sin repeticiones.
Autor: Adrian Alvarez
Fecha: 05/NOV/26
"""
import sys

lista_numeros = []

numero = 0
respuesta_usuario = ""

while True:
    try:
        numero = int(input("Ingrese un número entero para añadirlo a la lista: "))
        lista_numeros.append(numero)
        
        respuesta_usuario = input("¿Desea agregar otro número? S/s para sí, N/n para no: ").lower()
        while respuesta_usuario != "s" and respuesta_usuario != "n":
            print("Error: Debe ingresar una de las opciones disponibles.", file=sys.stderr)
            respuesta_usuario = input("Inténtelo de nuevo: ")

        if respuesta_usuario == "n":
            break
    except ValueError:
        print("Error: El valor ingresado debe ser un número entero. Inténtelo de nuevo.", file=sys.stderr)

lista_numeros.sort()

print(f"La primera lista es: {lista_numeros}")

lista_numeros_ordenada = []

for numero in lista_numeros:
    while lista_numeros.count(numero) > 1:
        lista_numeros.remove(numero)
    else:
        lista_numeros_ordenada.append(numero)

print(f"La segunda lista es: {lista_numeros_ordenada}")