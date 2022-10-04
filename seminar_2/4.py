import random

n = int(input("Введите N: "))
if n == 0:
    print("Так дело не пойдёт!\n")
    exit()
if n < 0:
    n *= -1

list = [i for i in range(-n, n + 1)]


index_list = []
j = 0

while len(index_list) < len(list) / 2:
    j = random.randint(0, len(list) - 1)
    if j not in index_list:
        index_list.append(j)

with open("seminar_2/file.txt", "w") as file:
    for i in range(len(index_list)):
        if i < len(index_list) - 1:
            file.write(f"{index_list[i]}\n")
        else:
            file.write(f"{index_list[i]}")

list_readed = []
with open("seminar_2/file.txt") as file:
    list_readed = file.read().splitlines()

mult = 1

for i in range(len(list_readed)):
    j = int(list_readed[i])
    if list[j] == 0:
        mult += 0
    else:
        mult *= list[j]
print(mult)
