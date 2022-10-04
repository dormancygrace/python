n = int(input("Введите N: "))
if n <= 0:
    print("Вы ввели ненатуральное число\n")
    exit()

dict = {}
dict = \
    {
        x: (3 * x) + 1 for x in range(1, n+1)
    }

print(dict)