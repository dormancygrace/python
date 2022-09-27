x = int(input("Введите координату X не равную 0 \n"))
y = int(input("Введите координату Y не равную 0 \n"))

if x == 0 or y == 0:
    print("Одна из координат равна 0. Это печально")
elif x > 0 and y > 0:
    print(f'x = {x}; y = {y} -> I')
elif x < 0 and y > 0:
    print(f'x = {x}; y = {y} -> II')
elif x < 0 and y < 0:
    print(f'x = {x}; y = {y} -> III')
elif x > 0 and y < 0:
    print(f'x = {x}; y = {y} -> IV')