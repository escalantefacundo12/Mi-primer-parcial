"""Escribe un programa que calcule el sueldo de un empleado basándose en la cantidad de horas y muestre
por pantalla el resultado, considerando lo siguiente:
a. Si trabajo más de 120hs por mes, la hora tiene un valor de $1500.
b. Si trabajo entre 80 y 120hs por mes, la hora tiene un valor de $1300.
c. Si trabajo menos de 80 horas por mes, la hora tiene un valor de $1100."""

# Solicitamos la cantidad de horas trabajadas al usuario
horas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

# Verificamos si se supera el límite de horas
if horas > 192:
    print("Has superado el límite de horas permitido.")
else:
    # Calculamos el valor de la hora según la cantidad de horas trabajadas
    if horas > 120:
        valor_hora = 1500
    elif horas >= 80:
        valor_hora = 1300
    else:
        valor_hora = 1100
    
    # Calculamos el sueldo total
    sueldo_total = valor_hora * horas
    
    # Mostramos el resultado
    print("El sueldo total del empleado es: $", sueldo_total)

