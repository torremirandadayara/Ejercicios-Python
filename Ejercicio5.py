import random

list = []
for indice in range(1, 11):
    list.append(random.randint(1, 10))

list.sort()

for num in list:
    print(num, " ", end="")
