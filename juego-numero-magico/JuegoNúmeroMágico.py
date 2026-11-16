"""
Archivo: JuegoNúmeroMágico
Descripción: Programa que lleva a cabo el juego del número mágico.
Autor: Adrian Alvarez
Fecha: 19/OCT/26
"""
import random

print("Juguemos al juego del número mágico! Tienes 5 intentos!")

numeroMagico = random.randint(1, 100)
numeroUsuario = int(input("¿En qué número estoy pensando?: "))

extremoMenor = 1
extremoMayor = 100
contadorIntentos = 1

while numeroUsuario != numeroMagico and contadorIntentos < 5:
    if numeroMagico < numeroUsuario:
        extremoMayor = numeroUsuario - 1
        print(f"Incorrecto. Te daré una pista, es un número menor y se encuentra entre: {extremoMenor} y {extremoMayor}.")
        contadorIntentos = contadorIntentos + 1
    
    elif numeroMagico > numeroUsuario:
        extremoMenor = numeroUsuario + 1
        print(f"Incorrecto. Te daré una pista, es un número mayor y se encuentra entre: {extremoMenor} y {extremoMayor}.")
        contadorIntentos = contadorIntentos + 1
    
    numeroUsuario = int(input("¿En qué número estoy pensando?: "))

if contadorIntentos >= 5 and numeroUsuario != numeroMagico:
    print("Perdiste!")

if numeroUsuario == numeroMagico:
    print("Increíble, adivinaste!")