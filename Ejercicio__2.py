"""scribe un programa que calcule el área y el perímetro de un cuadrado y muestre los resultados (indicando
cuál es cuál) por pantalla."""

# Solicitar la longitud del lado del cuadrado
lado = float(input("Ingrese la longitud del lado del cuadrado: "))

# Calcular el área del cuadrado
area = lado ** 2

# Calcular el perímetro del cuadrado
perimetro = 4 * lado

# Mostrar los resultados
print("El área del cuadrado es:",area)
print("El perímetro del cuadrado es:",perimetro)