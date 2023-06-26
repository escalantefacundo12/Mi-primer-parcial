# Inicializar variables
suma_calificaciones = 0
contador = 0

# Solicitar la cantidad de alumnos
alumnos_totales = int(input("Ingrese la cantidad de alumnos en la clase: "))

# Solicitar las calificaciones de los estudiantes
while contador < alumnos_totales:
    calificacion = float(input(f"Ingrese la calificación del estudiante {contador + 1}: "))
    if calificacion > 10:
        print("La calificación ingresada es inválida. Debe ser menor o igual a 10.")
    else:
        suma_calificaciones += calificacion
        contador += 1
        
# Calcular el promedio si se ingresaron calificaciones válidas
if contador > 0:
    promedio = suma_calificaciones / contador
    print("El promedio general de la clase es:", promedio)
else:
    print("No se ingresaron calificaciones válidas.")