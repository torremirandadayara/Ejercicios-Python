nombres = []
edades = []
while True:
    nombre = input("Escriba el nombre de un alumno:")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Introduzca su edad:")))
    if nombre == "*": break

print("------------------------")
edad_maxima = max(edades)
print("Todos los alumnos mayores de edad:")
for nombre, edad in zip(nombres, edades):
    if edad >= 18:
        print(nombre)

print("-----------------")
print("Alumnos mayores:")
for nombre, edad in zip(nombres, edades):
    if edad == edad_maxima:
        print(nombre)
