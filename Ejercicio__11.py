""". Escribe un programa que muestre los números del 1 al 10. Además, el programa debe mostrar:
a. Si es número es par o impar.
b. Cuanto es la suma total de todos los números mostrados.
c. Cuanto es la suma total de todos los números pares mostrados.
d. Cuanto es la suma total de todos los números impares mostrados."""

num = 1  # Inicializamos un contador num en 1
suma_total = 0  
suma_pares = 0  
suma_impares = 0  

while num <= 10:  
    print(num)  # Mostramos el número actual

    suma_total += num  # Acumulamos el número actual a la suma total

    if num % 2 == 0:  # Si el número es divisible entre 2 (es par)
        suma_pares += num 
        print("Es par")
    else:  # Si el número no es divisible entre 2 (es impar)
        suma_impares += num
        print("Es impar")

    num += 1  # Incrementamos el numero en 1 para pasar al siguiente número

print("La suma total de todos los números mostrados es:", suma_total)
print("La suma total de los números pares mostrados es:", suma_pares)
print("La suma total de los números impares mostrados es:", suma_impares)

