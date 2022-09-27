number = int(input('Введите число от 1 до 7 \n'))
if number < 1 or number > 7:
    print('В неделе от одного до семи дней =( ')
elif number == 6 or number == 7:
    print(f'{number}  -> да')
else: 
    print(f'{number} -> нет')
