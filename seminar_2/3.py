result = 0

n = int(input("Введите N: "))
if n <= 0:
    print("Вы ввели ненатуральное число\n")
    exit()

list = [(1 + (1 / i)) ** i for i in range(1, n + 1)]

for i in range(len(list)):
    result += list[i] 

print(round(result, 2))