# Solicitar la cantidad de horas trabajadas al usuario
horas = int(input("Ingrese la cantidad de horas trabajadas en el mes: "))

# Calcular el valor de la hora según la cantidad de horas trabajadas
if horas > 120:
    valor_hora = 1500
    bonificacion = 0.18
elif horas >= 80:
    valor_hora = 1300
    bonificacion = 0.15
else:
    valor_hora = 1100
    bonificacion = 0.13

# Calcular el sueldo bruto, la bonificación y el sueldo neto
sueldo_bruto = valor_hora * horas
monto_bonificacion = (sueldo_bruto * bonificacion) 
sueldo_neto = sueldo_bruto + monto_bonificacion

# Calcular el sueldo anual bruto, el monto anual de bonificaciones y el descuento anual
sueldo_anual_bruto = sueldo_bruto * 12
monto_bonificacion_anual = monto_bonificacion * 12

if sueldo_anual_bruto > 2000000:
    descuento_anual = (sueldo_anual_bruto *0.05) 
elif sueldo_anual_bruto >= 1000000:
    descuento_anual = (sueldo_anual_bruto *0.03) 
else:
    descuento_anual = (sueldo_anual_bruto  *0.01) 

# Calcular las horas trabajadas en todo el año
horas_anuales = horas * 12

# Mostrar los resultados
print("Sueldo Bruto Mensual: $", sueldo_bruto)
print("Bonificación Mensual: $", monto_bonificacion)
print("Sueldo Neto Mensual: $", sueldo_neto)
print("Sueldo Anual Bruto: $", sueldo_anual_bruto)
print("Monto Anual de Bonificaciones: $", monto_bonificacion_anual)
print("Descuento Anual: $", descuento_anual)
print("Horas Trabajadas en el Año: ", horas_anuales)
