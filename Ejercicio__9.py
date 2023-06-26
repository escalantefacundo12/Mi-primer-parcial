""". Escribe un programa que solicite y muestre por pantalla nombre, apellido y edad de una cantidad de
personas ingresada por el usuario."""

# Pedimos la cantidad de personas desea ingresar.
cantidad_personas = int(input("Ingresa la cantidad de personas: "))
contador = 1

# pedimos el nombre, apellido y edad de las personas.
while contador <= cantidad_personas:
    print("Persona", contador)
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")

    #mostramos el nombre, apellido y edad.
    print("Nombre:", nombre,)
    print("Apellido:", apellido)
    print("Edad:", edad)
    contador += 1
