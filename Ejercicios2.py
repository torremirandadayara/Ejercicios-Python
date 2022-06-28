lista1 = []
lista2 = []

for indice in range(1, 6):
    lista1.append(input("Escriba la cadena %d:" % indice))

lista2 = lista1[::-1]

for cadena in lista2:
    print(cadena)
