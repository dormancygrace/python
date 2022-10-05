import random

list = [random.randrange(-10, 11, 1) for i in range(5)]
mult = []
print(list)


for i in range(len(list)//2):
    mult.append(list[i] * list[len(list) - 1 - i])
if len(list) % 2 == 1: mult.append(list[i + 1] ** 2)

print(mult)
