import random

print("Piedra, papel o tijera! La humanidad contra las máquinas!")
# Obtener elección usuario
eleccionUsuario = int(input("Elija el número que represente su elección (1. Piedra, 2. Papel, 3. Tijera): "))
# Validar elección usuario
if eleccionUsuario >= 1 and eleccionUsuario <= 3:
    # Mostrar elección usuario
    if eleccionUsuario == 1:
        print("El humano eligió piedra!")
    elif eleccionUsuario == 2:
        print("El humano eligió papel!")
    else:
        print("El humano eligió tijera!")
    # Obtener elección máquina
    eleccionMaquina = random.randint(1, 3)
    # Mostrar elección máquina
    if eleccionMaquina == 1:
        print("La máquina eligió piedra!")
    elif eleccionMaquina == 2:
        print("La máquina eligió papel!")
    else:
        print("La máquina eligió tijera!")
    # Batalla
    if eleccionUsuario == eleccionMaquina:
        print("Es un empate!")
    elif (eleccionUsuario == 1 and eleccionMaquina == 3) or (eleccionUsuario == 2 and eleccionMaquina == 1) or (eleccionUsuario == 3 and eleccionMaquina == 2):
        print("La humanidad gana!")
    else:
        print("Las máquinas ganan!")
else:
    print("Debe elegir una de las opciones disponibles. Inténtelo de nuevo.")