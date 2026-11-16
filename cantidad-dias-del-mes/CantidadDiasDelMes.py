"""
Archivo: CantidadDiasDelMes
Descripción: Programa que, dado un año (>1582) y un mes (1:Enero, 2:Febrero,…, 12:Diciembre), indica el número de días de ese mes en ese año.
Autor: Adrian Alvarez
Fecha: 14/OCT/26
"""

print("Programa que, dado un año (>1582) y un mes (1:Enero, 2:Febrero,…, 12:Diciembre), indica el número de días de ese mes en ese año.")

añoIngresado = int(input("Ingrese el año: "))

if añoIngresado > 1582:
    mesIngresado = int(input("Ahora, el dígito que represente al mes de su elección (1:Enero, 2:Febrero, 3:Marzo, 4:Abril, 5:Mayo, 6:Junio, 7:Julio, 8:Agosto, 9:Septiembre, 10:Octubre, 11:Noviembre, 12:Diciembre): "))
    match mesIngresado:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                print("Tiene 31 días")
            case 2: # Revisar si es año bisiesto o no.
                if (añoIngresado % 4 == 0 and añoIngresado % 100 != 0) or (añoIngresado % 400 == 0):
                   print("Tiene 29 días")
                else:
                   print("Tiene 28 días")
            case 4 | 6 | 9 | 11:
                print("Tiene 30 días")
            case _ :
                print("Tiene que ser un mes válido. Inténtelo de nuevo.")
else:
    print("En esa época se usaba un calendario distinto al que conocemos en la actualidad.")