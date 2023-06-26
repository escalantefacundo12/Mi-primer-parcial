"""Del punto anterior, calcular y mostrar por pantalla el sueldo bruto, el monto a bonificar y el sueldo neto
(bruto + bonif), considerando:
a. Si trabajo más de 120hs, la bonificación es de %18
b. Si trabajo entre 80 y 120 horas, la bonificación es de %15
c. Si trabajo menos de 80 horas, la bonificación es de %13."""

# Solicitamos la cantidad de horas trabajadas
horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))
# Definimos los valores de las horas y bonificaciones según las condiciones
if horas_trabajadas > 192:
    print("Error: La cantidad de horas trabajadas supera el límite permitido.")
else:
    if horas_trabajadas > 120:
        valor_hora = 1500
        bonificacion = 0.18
    elif horas_trabajadas >= 80 and horas_trabajadas <= 120:
        valor_hora = 1300
        bonificacion = 0.15
    elif horas_trabajadas < 80:
        valor_hora = 1100
        bonificacion = 0.13
    else:
        print("Error: La cantidad de horas trabajadas es inválida.")
        exit()
    # Calculamos el sueldo bruto
    sueldo_bruto = horas_trabajadas * valor_hora
    # Calculamos el monto a bonificar
    monto_bonificacion = sueldo_bruto * bonificacion
    # Calcular el sueldo neto
    sueldo_neto = sueldo_bruto + monto_bonificacion
    # Mostramos los resultados
    print("Sueldo bruto: $",sueldo_bruto)
    print("Monto a bonificar:$",monto_bonificacion)
    print("Sueldo neto:$",sueldo_neto)
