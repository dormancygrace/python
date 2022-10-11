import math

d = int(input("Введите желаемое количество знаков после запятой "))
if d <= 0:
    print("нет, так дело не пойдет")
    exit()

print("{:.{}f}".format(math.pi, d))