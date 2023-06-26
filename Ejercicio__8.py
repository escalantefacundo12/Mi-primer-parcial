""". Escribe un programa solicite y muestre por pantalla el nombre, apellido y edad de 5 personas"""

contador = 1
# Perdir al usuario que ingrese el nombre, apellido y edad.
while contador <= 5:
    print("Persona", contador)
    nombre = str(input("Ingresa tu nombre: "))
    apellido = str(input("Ingresa tu apellido: "))
    edad = str(input("Ingresa tu edad: "))
    
    # Mostrar el nombre, apellido y edad
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Edad:", edad)
    contador += 1