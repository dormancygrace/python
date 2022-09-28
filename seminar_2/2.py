n = int(input("Введите N: "))
result = 1

if n < 0:
    for i in range (1, n - 1, -1):
        if i != 0:
            if result < 0:
                result *= -1
            result *= i
            print(result)
        else:
            result = 0
            print(result)
            result = 1
elif n >= 1:
    for i in range(n):
        result *= i + 1
        print(result)