lista_1 = []
lista_2 = []
lista_3 = []
for indice in range(1, 6):
    lista_1.append(int(input("Introduce el %d valor del vector1:" % indice)))
for indice in range(1, 6):
    lista_2.append(int(input("Introduce el %d valor del vector2:" % indice)))

for indice in range(0, 5):
    lista_3.append(lista_1[indice] + lista_2[indice])

print("La suma es:")
for numero in lista_3:
    print(numero, " ", end="")
