"""Escribe un programa que calcule la edad que cumplió o debe cumplir este año la persona, basado en el
año de nacimiento."""
anio_actual = 2023  # Año actual (puedes cambiarlo según la fecha actual)

# Solicitar al usuario el año de nacimiento
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))

# Calcular y mostrar la edad
edad = anio_actual - anio_nacimiento
print("Este año tu cumples o cumpliras:", edad, "años" )