# Задана натуральная степень k.Сформировать случайным
# образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

import random


def write_file(st):
    with open('file_task3.txt', 'w') as data:
        data.write(st)


def create_mn(n):
    array = []
    for i in range(n):
        array.append(random.randint(0, 101))
    return array


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += (f'{lst[i]}x^{len(lst) - i - 1}')
                if (lst[i + 1]) != 0:
                    wr += (' + ')
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += (f'{lst[i]}x')
                if lst[i + 1] != 0:
                    wr += (' + ')
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += (f'{lst[i]} = 0')
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += (' = 0')
    return wr


try:
    k = int(input("Введите натуральную степень k = "))
    kof = create_mn(k)
    write_file(create_str(kof))
except:
    print("Введите целое число")
