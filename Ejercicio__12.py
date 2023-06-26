""". Escribe un programa que permita ingresar las edades de las personas, hasta que el usuario decida no
hacerlo más, y muestre, al final, un promedio de las edades ingresadas y el total de personas ingresadas."""

# Iniciar variables
suma_edades = 0
contador = 0
continuar = 1

# Solicitamos las edades de las personas
while continuar == 1:
    edad = input("Ingrese la edad de una persona (o 'q' para salir): ")

    if edad == 'q' or edad == 'Q':
        continuar = 0
    else:
        edad = int(edad)
        suma_edades += edad
        contador += 1

    # Verificamos si se debe continuar o salir del bucle
    if contador >= 100:
        print("Se ha alcanzado el límite máximo de personas.")
        continuar = 0

# Calculamos el promedio si se ingresaron edades
if contador > 0:
    promedio = suma_edades / contador
    print("Promedio de edades:", promedio)
    print("Total de personas ingresadas:", contador)
else:
    print("No se ingresaron edades.")