from time import time

list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def mix_list(old: list) -> list:
    new = []
    while old:
        x = str(time()).split(".")[1]
        x = list(map(int, [x[0], x[-1]]))
        x = x[0] if x[0] <= x[1] else x[1]
        if x > len(old) - 1:
            new.append(old.pop(0))
        else:
            new.append(old.pop(x))
    return new


list0 = mix_list(list0)
print(list0)
