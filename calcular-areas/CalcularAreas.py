"""
Archivo: CalcularAreas
Descripción: Programa que calcula el área de un triángulo, círculo o un rectángulo, hasta que el usuario desee "Salir".
Autor: Adrian Alvarez
Fecha: 19/OCT/26
"""
import math

print("Programa que calcula el área de un triángulo, círculo o un rectángulo.")

# Obtener elección del usuario
eleccionUsuario = int(input("¿Qué desea hacer?, ¿Calcular el área de un triángulo (1), el área de un círculo (2), el área de un rectángulo (3), o salir del programa (0)?: "))
# Validar elección del usuario
while eleccionUsuario < 0 or eleccionUsuario > 3:
    eleccionUsuario = int(input("Debe elegir una de las opciones disponibles. Inténtelo de nuevo: "))
# Mostrar mensaje de despedida
if eleccionUsuario == 0:
    print("Gracias por usar este programa.")

while eleccionUsuario != 0:
    
    if eleccionUsuario == 1:
        # Obtener base del triángulo
        baseTriangulo = float(input("Ingrese la base del triángulo en centímetros: "))
        # Validar base del triángulo        
        while baseTriangulo <= 0:
            baseTriangulo = float(input("Debe ser un valor positivo mayor a 0. Inténtelo de nuevo: "))
        
        # Obtener altura del triángulo
        alturaTriangulo = float(input("Ingrese la altura del triángulo en centímetros: "))
        # Validar altura del triángulo
        while alturaTriangulo <= 0:
            alturaTriangulo = float(input("Debe ser un valor positivo mayor a 0. Inténtelo de nuevo: "))
        
        # Mostrar área del triángulo
        print(f"El área del triángulo es: {(baseTriangulo * alturaTriangulo) / 2:.2f} centímetros cuadrados.")
        
        # Obtener nueva elección del usuario
        eleccionUsuario = int(input("¿Qué desea hacer?, ¿Calcular el área de un triángulo (1), el área de un círculo (2), el área de un rectángulo (3), o salir del programa (0)?: "))
        # Validar nueva elección del usuario
        while eleccionUsuario < 0 or eleccionUsuario > 3:
            eleccionUsuario = int(input("Debe elegir una de las opciones disponibles. Inténtelo de nuevo: "))
        # Mostrar mensaje de despedida
        if eleccionUsuario == 0:
            print("Gracias por usar este programa.")
    
    if eleccionUsuario == 2:
        # Obtener radio del círculo
        radioCirculo = float(input("Ingrese el radio del círculo en centímetros: "))
        # Validar radio del círculo
        while radioCirculo <= 0:
            radioCirculo = float(input("Debe ser un valor positivo mayor a 0. Inténtelo de nuevo: "))
        
        # Mostrar área del círculo
        print(f"El área del círculo es: {math.pi * (radioCirculo**2):.2f} centímetros cuadrados.")
        
        # Obtener nueva elección del usuario
        eleccionUsuario = int(input("¿Qué desea hacer?, ¿Calcular el área de un triángulo (1), el área de un círculo (2), el área de un rectángulo (3), o salir del programa (0)?: "))
        # Validar nueva elección del usuario
        while eleccionUsuario < 0 or eleccionUsuario > 3:
            eleccionUsuario = int(input("Debe elegir una de las opciones disponibles. Inténtelo de nuevo: "))
        # Mostrar mensaje de despedida
        if eleccionUsuario == 0:
            print("Gracias por usar este programa.")
    
    if eleccionUsuario == 3:
        # Obtener base del rectángulo
        baseRectangulo = float(input("Ingrese la base del rectángulo en centímetros: "))
        # Validar base del rectángulo
        while baseRectangulo <= 0:
            baseRectangulo = float(input("Debe ser un valor positivo mayor a 0. Inténtelo de nuevo: "))
        
        # Obtener altura del rectángulo
        alturaRectangulo = float(input("Ingrese la altura del rectángulo en centímetros: "))
        # Validar altura del rectángulo
        while alturaRectangulo <= 0:
            alturaRectangulo = float(input("Debe ser un valor positivo mayor a 0. Inténtelo de nuevo: "))
        
        # Mostrar área del rectángulo
        print(f"El área del rectángulo es: {baseRectangulo * alturaRectangulo:.2f} centímetros cuadrados.")
        
        # Obtener nueva elección del usuario
        eleccionUsuario = int(input("¿Qué desea hacer?, ¿Calcular el área de un triángulo (1), el área de un círculo (2), el área de un rectángulo (3), o salir del programa (0)?: "))
        # Validar nueva elección del usuario
        while eleccionUsuario < 0 or eleccionUsuario > 3:
            eleccionUsuario = int(input("Debe elegir una de las opciones disponibles. Inténtelo de nuevo: "))
        # Mostrar mensaje de despedida
        if eleccionUsuario == 0:
            print("Gracias por usar este programa.")