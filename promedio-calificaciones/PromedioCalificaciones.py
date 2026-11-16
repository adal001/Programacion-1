"""
Archivo: PromedioCalificaciones
Descripción: Programa que calcula el promedio de n calificaciones dadas en el rango [0, 100]. El valor n es un entero positivo.
Autor: Adrian Alvarez
Fecha: 15/OCT/26
"""
import sys

print("Programa que calcula el promedio de n calificaciones dadas en el rango [0, 100].")

sumaCalif = 0
numCalif = 0

calif = float(input("Ingrese una calificación: "))

while calif < 0 or calif > 100:
    calif = float(input("Debe ser un valor entre 0 y 100. Inténtelo de nuevo: "))
    
sumaCalif += calif
numCalif += 1

continuarIngresando = True

while continuarIngresando == True:
    respuestaUsuario = input("Si desea agregar otra calificación, presione 's', de otro modo, 'n': ").lower()
    
    while respuestaUsuario != "s" and respuestaUsuario != "n":
        respuestaUsuario = input("Debe ingresar un carácter válido. Inténtelo de nuevo: ")
        respuestaUsuario.lower()

    while respuestaUsuario == "s":
        calif = float(input("Ingrese la siguiente calificación: "))
        while calif < 0 or calif > 100:
            calif = float(input("Debe ser un valor entre 0 y 100. Inténtelo de nuevo: "))
        sumaCalif += calif
        numCalif += 1
        
        respuestaUsuario = input("Si desea agregar otra calificación, presione 's', de otro modo, 'n': ").lower()
    
        while respuestaUsuario != "s" and respuestaUsuario != "n":
            respuestaUsuario = input("Debe ingresar un carácter válido. Inténtelo de nuevo: ")
            respuestaUsuario.lower()
        
        if respuestaUsuario == "n":
            respuestaUsuario = "n"

    if respuestaUsuario == "n":
        continuarIngresando = False

promedio = sumaCalif / numCalif
print(f"El promedio es: {promedio:.2f}.")