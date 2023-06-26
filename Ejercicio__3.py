"""Escribe un programa que calcule la equivalencia a pesos de los dólares ingresados por pantalla. El
programa debe preguntar el tipo de cambio a convertir (es decir, cuánto cotiza el dólar)."""

# Solicitamos cuantos dolares desea ingresar
monto_dolares = float(input("cuantos dolares desea ingresar?: "))

# Solicitamos el tipo de cambio
tipo_cambio = float(input("Ingrese el tipo de cambio: "))

# Calculamos la equivalencia en pesos
monto_pesos = monto_dolares * tipo_cambio

# Mostra,os el resultado
print("Equivalente en pesos:",monto_pesos, "pesos")