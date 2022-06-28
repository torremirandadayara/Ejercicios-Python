lista = []
num = int(input("Introduce un número en la lista:"))
while num >= 0:
    lista.append(num)
    num = int(input("Introduce un número en la lista:"))

for num in lista:
    print(num, " ", end="")
