import random

list = [round(random.uniform(-10.00, 10.00), 2) for i in range(10)]

for i in range(len(list)):
    list[i] = round(int(list[i]) - list[i], 2)

result = round(max(list) - min(list), 2)
print(result)