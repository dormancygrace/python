n = int(input("Введите N: "))
result = 1
zero_case = 0

if n < 0:
    for i in range (1, n - 1, -1):
        if i != 0 and i != n:
            if result < 0:
                result *= -1
            result *= i
            print(result, end = ', ')
        elif i == n:
            if result < 0:
                result *= -1
            result *= i
            print(result, end = '.')
        else:
            result *= i
            print(result, end = ', ')
            result += 1
elif n >= 1:
    for i in range(n):
        if i != n - 1:
            result *= i + 1
            print(result, end = ', ')
        else:
            result *= i + 1
            print(result, end = '.')