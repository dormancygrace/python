import math

d = int(input("Введите желаемое количество знаков после запятой "))

print("{:.{}f}".format(math.pi, d))