quarter = int(input("Введите номер четверти \n"))

if quarter < 1 or quarter > 4:
    print("Что же это за четверть такая?")

elif quarter == 1:
    print("X и Y больше 0")
elif quarter == 2:
    print("X меньше 0, Y больше 0")
elif quarter == 3:
    print("X и Y меньше 0")
else:
    print("X больше 0, Y меньше 0")