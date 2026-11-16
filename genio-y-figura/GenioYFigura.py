"""
Archivo: GenioYFigura.py
Descripción: Programa que imprime figuras rellenas (reloj de arena, rombo, moño, copa).
Grupo 11: Adrian Alvarez y Geovanni Morales
Fecha de entrega: 03/NOV/26
"""

# FUNCIONES ############################################################################

def RelojArena(dimension:int, simbolo:str):
    """
    Imprime la figura de un reloj de arena creada con datos proporcionados por el usuario.
    
    Parameters:
        dimension(int): Número utilizado para definir el tamaño de la figura.
        simbolo(str): Carácter utilizado para crear la figura.
    
    Raises:
        TypeError: Si dimension no es un entero.
        TypeError: Si simbolo no es una cadena.
    """
    if not isinstance(dimension, int):
        raise TypeError("El argumento dimension debe ser un entero.")

    if not isinstance(simbolo, str):
        raise TypeError("El argumento simbolo debe ser una cadena.")
    
    # Primera parte de la figura:
    for i in range(dimension, 0, -2):
        print(f"{i*simbolo:^{dimension}}")
    # Segunda parte de la figura:
    for i in range(3, dimension+1, 2):
        print(f"{i*simbolo:^{dimension}}")
    
    print()

def Rombo(dimension:int, simbolo:str):
    """
    Imprime la figura de un rombo creada con datos proporcionados por el usuario.
    
    Parameters:
        dimension(int): Número utilizado para definir el tamaño de la figura.
        simbolo(str): Carácter utilizado para crear la figura.
    
    Raises:
        TypeError: Si dimension no es un entero.
        TypeError: Si simbolo no es una cadena.
    """
    if not isinstance(dimension, int):
        raise TypeError("El argumento dimension debe ser un entero.")

    if not isinstance(simbolo, str):
        raise TypeError("El argumento simbolo debe ser una cadena.")
    
    # Primera parte de la figura:
    for i in range(1, dimension+1, 2):
        print(f"{i*simbolo:^{dimension}}")
    # Segunda parte de la figura:
    for i in range(dimension-2, 0, -2):
        print(f"{i*simbolo:^{dimension}}")
    
    print()

def Monio(dimension:int, simbolo:str):
    """
    Imprime la figura de un moño creada con datos proporcionados por el usuario.
    
    Parameters:
        dimension(int): Número utilizado para definir el tamaño de la figura.
        simbolo(str): Carácter utilizado para crear la figura.
    
    Raises:
        TypeError: Si dimension no es un entero.
        TypeError: Si simbolo no es una cadena.
    """
    if not isinstance(dimension, int):
        raise TypeError("El argumento dimension debe ser un entero.")

    if not isinstance(simbolo, str):
        raise TypeError("El argumento simbolo debe ser una cadena.")
    
    # Parte superior de la figura:
    for i in range(1, (dimension//2)+1):
        print(i*simbolo + (dimension-(2*i))*" " + i*simbolo)

    # Parte central de la figura:
    print(dimension*simbolo)

    # Parte inferior de la figura:
    for i in range(dimension//2, 0, -1):
        print(i*simbolo + (dimension-(2*i))*" " + i*simbolo)
    
    print()

def Copa(dimension:int, simbolo:str):
    """
    Imprime la figura de una copa creada con datos proporcionados por el usuario.
    
    Parameters:
        dimension(int): Número utilizado para definir el tamaño de la figura.
        simbolo(str): Carácter utilizado para crear la figura.
    
    Raises:
        TypeError: Si dimension no es un entero.
        TypeError: Si simbolo no es una cadena.
    """
    if not isinstance(dimension, int):
        raise TypeError("El argumento dimension debe ser un entero.")

    if not isinstance(simbolo, str):
        raise TypeError("El argumento simbolo debe ser una cadena.")

    # Cáliz:
    for i in range(dimension, 0, -2):
        print(f"{i*simbolo:^{dimension}}")

    # Tallo:
    for i in range(3):
        print(f"{simbolo:^{dimension}}")

    # Base:
    print(dimension*simbolo)
    
    print()
    
# PROCESO PRINCIPAL ####################################################################

import sys

print("Programa que imprime la figura elegida por el usuario.\n")

eleccionUsuario = 0
# Entrar al programa
while eleccionUsuario != 6:
    print("Opciones disponibles:\n1)Reloj de arena, 2)Rombo, 3)Moño, 4)Copa, 5)Todas las anteriores, 6)Salir del programa.\n")
    # Obtener elección del usuario y validarla
    while True:
        try:
            eleccionUsuario = int(input("Ingrese el número correspondiente a la figura que desee imprimir: "))
            break
        except ValueError:
            print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    # Obtener la dimensión y el símbolo, validarlos, y mostrar la figura elegida por el usuario
    if eleccionUsuario == 1:
        
        while True:
            try:
                dimension = int(input("Ingrese la dimensión que tendrá la figura: "))
                
                if dimension % 2 != 0 and dimension >= 5 and dimension <= 19:
                    break
                else:
                    print("Error: El valor de la dimensión debe ser un número impar entre 5 y 19 inclusive. Inténtelo de nuevo.", file=sys.stderr)
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    
        simbolo = input("Ingrese el símbolo con el cual se elaborará la figura: ")
        while len(simbolo) != 1 or simbolo == " ":
            print("Error: Debe ingresar un único carácter que no sea un espacio en blanco.", file=sys.stderr)
            simbolo = input("Inténtelo de nuevo: ")

        RelojArena(dimension, simbolo)
    
    elif eleccionUsuario == 2:
        
        while True:
            try:
                dimension = int(input("Ingrese la dimensión que tendrá la figura: "))
                
                if dimension % 2 != 0 and dimension >= 5 and dimension <= 19:
                    break
                else:
                    print("Error: El valor de la dimensión debe ser un número impar entre 5 y 19 inclusive. Inténtelo de nuevo.", file=sys.stderr)
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    
        simbolo = input("Ingrese el símbolo con el cual se elaborará la figura: ")
        while len(simbolo) != 1 or simbolo == " ":
            print("Error: Debe ingresar un único carácter que no sea un espacio en blanco.", file=sys.stderr)
            simbolo = input("Inténtelo de nuevo: ")

        Rombo(dimension, simbolo)
    
    elif eleccionUsuario == 3:
        
        while True:
            try:
                dimension = int(input("Ingrese la dimensión que tendrá la figura: "))
                
                if dimension % 2 != 0 and dimension >= 5 and dimension <= 19:
                    break
                else:
                    print("Error: El valor de la dimensión debe ser un número impar entre 5 y 19 inclusive. Inténtelo de nuevo.", file=sys.stderr)
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    
        simbolo = input("Ingrese el símbolo con el cual se elaborará la figura: ")
        while len(simbolo) != 1 or simbolo == " ":
            print("Error: Debe ingresar un único carácter que no sea un espacio en blanco.", file=sys.stderr)
            simbolo = input("Inténtelo de nuevo: ")

        Monio(dimension, simbolo)
    
    elif eleccionUsuario == 4:
        
        while True:
            try:
                dimension = int(input("Ingrese la dimensión que tendrá la figura: "))
                
                if dimension % 2 != 0 and dimension >= 5 and dimension <= 19:
                    break
                else:
                    print("Error: El valor de la dimensión debe ser un número impar entre 5 y 19 inclusive. Inténtelo de nuevo.", file=sys.stderr)
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    
        simbolo = input("Ingrese el símbolo con el cual se elaborará la figura: ")
        while len(simbolo) != 1 or simbolo == " ":
            print("Error: Debe ingresar un único carácter que no sea un espacio en blanco.", file=sys.stderr)
            simbolo = input("Inténtelo de nuevo: ")

        Copa(dimension, simbolo)
    
    elif eleccionUsuario == 5:
        
        while True:
            try:
                dimension = int(input("Ingrese la dimensión que tendrán la figuras: "))
                
                if dimension % 2 != 0 and dimension >= 5 and dimension <= 19:
                    break
                else:
                    print("Error: El valor de la dimensión debe ser un número impar entre 5 y 19 inclusive. Inténtelo de nuevo.", file=sys.stderr)
            except ValueError:
                print("Error: Debe ingresar un número entero. Inténtelo de nuevo.", file=sys.stderr)
    
        simbolo = input("Ingrese el símbolo con el cual se elaborarán la figuras: ")
        while len(simbolo) != 1 or simbolo == " ":
            print("Error: Debe ingresar un único carácter que no sea un espacio en blanco.", file=sys.stderr)
            simbolo = input("Inténtelo de nuevo: ")
        
        RelojArena(dimension, simbolo)
        Rombo(dimension, simbolo)
        Monio(dimension, simbolo)
        Copa(dimension, simbolo)
    
    elif eleccionUsuario == 6:
        print("Gracias por haber utilizado este programa.")
    
    else:
        print("Debe elegir una de las opciones disponibles. Intételo de nuevo.\n")