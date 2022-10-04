result = 0

n = int(input("Введите N: "))
if n <= 0:
    print("Вы ввели ненатуральное число\n")
    exit()

list = [(1 + (1 / n)) ** n for i in range(1, n +1)]

print(round(list[0]*n, 2))