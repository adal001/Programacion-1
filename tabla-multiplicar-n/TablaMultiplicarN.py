"""
Archivo: TablaMultiplicarN
Descripción: Programa que lee un entero n y escribe la tabla de multiplicar de n (de 1 a 10).
Autor: Adrian Alvarez
Fecha: 19/OCT/26
"""

print("Programa que lee un entero n y escribe la tabla de multiplicar de n (de 1 a 10).")

n = int(input("Ingrese un número para obtener su tabla de multiplicar: "))

while n < 1:
    n = int(input("El número a ingresar debe ser mayor que 0. Inténtelo de nuevo: "))

print(f"""
Tabla de multiplicar de {n}:
{n} x 1 = {n * 1}
{n} x 2 = {n * 2}
{n} x 3 = {n * 3}
{n} x 4 = {n * 4}
{n} x 5 = {n * 5}
{n} x 6 = {n * 6}
{n} x 7 = {n * 7}
{n} x 8 = {n * 8}
{n} x 9 = {n * 9}
{n} x 10 = {n * 10}
""")