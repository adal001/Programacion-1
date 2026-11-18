# Programa que captura el nombre, la edad y el peso del usuario y los imprime juntos con el formato:
# XXXXXXXXX, tienes XX años y pesas XX.XX kg.

nombreUsuario = input("Ingrese su nombre: ")
edadUsuario = input("Ahora su edad: ")
# Obtener número entero y convertirlo a número real.
pesoUsuario = float(input("Y por último, su peso en kg: "))

print(nombreUsuario, ", tienes ", edadUsuario, " años y pesas ", pesoUsuario, " kg.", sep="")