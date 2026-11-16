"""
Archivo: FormatoFecha
Descripción: Programa que, dados tres números enteros correspondientes a una fecha de nacimiento: año, mes, día,
             obtiene una cadena de longitud 6, donde los dos primeros caracteres son los dos últimos dígitos del año,
             los siguientes dos corresponden al mes (0x para meses de 1 dígito) y los últimos dos corresponden al día (0x para días de 1 dígito).
Autor: Adrian Alvarez
Fecha: 21/OCT/26
"""

print("Programa que obtiene una fecha de nacimiento y la devuelve en un formato específico.")
print()

# Obtener y validar año
anio = int(input("Ingrese un año entre 1900 y 2026: "))
while not 1900 <= anio <= 2026:
    anio = int(input("Debe ingresar un año entre 1900 y 2026. Inténtelo de nuevo: "))
print()

# Obtener y validar mes
print("1)Enero, 2)Febrero, 3)Marzo, 4)Abril, 5)Mayo, 6)Junio, 7)Julio, 8)Agosto, 9)Septiembre, 10)Octubre, 11)Noviembre, 12)Diciembre.")
mes = int(input("Ingrese un número entre 1 y 12, correspondiente al mes de su elección: "))
while not 1 <= mes <= 12:
    mes = int(input("Debe ingresar un número de mes válido. Inténtelo de nuevo: "))
print()

# Obtener y validar día
match mes:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        dia = int(input("Ingrese el número del día entre 1 y 31: "))
        while not 1 <= dia <= 31:
            dia = int(input("Debe ingresar un número de día válido. Inténtelo de nuevo: "))
    case 4 | 6 | 9 | 11:
        dia = int(input("Ingrese el número del día entre 1 y 30: "))
        while not 1 <= dia <= 30:
            dia = int(input("Debe ingresar un número de día válido. Inténtelo de nuevo: "))
    case 2:
        if anio % 4 == 0 and anio % 100 != 0 or anio % 400 == 0:
            dia = int(input("Ingrese el número del día entre 1 y 29: "))
            while not 1 <= dia <= 29:
                dia = int(input("Debe ingresar un número de día válido. Inténtelo de nuevo: "))
        else:
            dia = int(input("Ingrese el número del día entre 1 y 28: "))
            while not 1 <= dia <= 28:
                dia = int(input("Debe ingresar un número de día válido. Inténtelo de nuevo: "))
print()

# Convertir valores enteros a cadena y construir la fecha en su nuevo formato
anio = str(anio)
primerosDosCaracteres = anio[2:]

mes = str(mes)
if len(mes) == 2:
    siguientesDosCaracteres = mes[0:]
elif len(mes) == 1:
    siguientesDosCaracteres = "0" + mes

dia = str(dia)
if len(dia) == 2:
    ultimosDosCaracteres = dia[0:]
elif len(dia) == 1:
    ultimosDosCaracteres = "0" + dia

fechaNuevoFormato = primerosDosCaracteres + siguientesDosCaracteres + ultimosDosCaracteres
print(f"La fecha de nacimiento en su nuevo formato es: {fechaNuevoFormato}.")