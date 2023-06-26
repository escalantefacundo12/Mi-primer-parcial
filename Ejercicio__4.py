"""Escribe un programa que calcule el promedio final de una materia, basado en 3 notas de parciales,
indicando por pantalla si el alumno aprobó o debe recursar la materia (se aprueba con 6)."""

# Solicitar las notas de los parciales
nota1 = float(input("Ingrese la nota del primer parcial: "))
nota2 = float(input("Ingrese la nota del segundo parcial: "))
nota3 = float(input("Ingrese la nota del tercer parcial: "))

# Calculamos el promedio
promedio = (nota1 + nota2 + nota3) / 3

# Mostramos el promedio
print("Promedio final:",promedio)

# Verificamos si el alumno aprobó o debe recursar
if promedio >= 6:
    print("El alumno aprobó la materia.")
else:
    print("El alumno debe recursar la materia.")
