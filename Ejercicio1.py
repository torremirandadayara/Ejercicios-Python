import random

listanum = []
for indice in range(1, 11):
    listanum.append(random.randint(1, 10))
for num in listanum:
    print(num, " ", num ** 2, " ", num ** 3)
