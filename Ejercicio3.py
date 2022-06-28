notas = []
for indice in range(1, 6):
    while True:
        nota = int(input("Introduce la nota %d:" % indice))
        if 0 <= nota <= 10: break
    notas.append(nota)
print("--------------------------")
print("Nota media: ", sum(notas) / len(notas))
print("Nota mas alta: ", max(notas))
print("Nota menor: ", min(notas))
