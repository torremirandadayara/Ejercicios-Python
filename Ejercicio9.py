temperaturas = []
for indice in range(1, 6):
    temperatura = [int(input("Día %d. Temperatura máxima:" % indice)),
                   int(input("Día %d. Temperatura mínima:" % indice))]
    temperaturas.append(temperatura)

print("--------------------")
print("Temperatura medias de cada dia:")

indice = 1
for temperatura in temperaturas:
    print("Día %d. Temperatura media: %f:" % (indice, sum(temperatura) / len(temperatura)))
    indice += 1

temp_min = temperaturas[0][1]
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]

print("--------------------------")
print("Los dias con menos temperatura:")
indice = 1
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print("-Día %d" % indice)
    indice += 1

existe_temperatura = False
print("---------------------------")
print("Días con temperatura máxima")
temp_max = int(input("Introduce una temperatura:"))
indice = 1
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print("-Día %d" % indice)
        existe_temperatura = True
    indice += 1
if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")
