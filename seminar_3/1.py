import random

list = [random.randrange(-10, 11, 1) for i in range(12)]
sum = 0

print(list)

for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(sum)