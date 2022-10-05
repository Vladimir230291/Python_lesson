# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random


def create_array(arg):
    arr = []
    for i in range(arg):
        arr.append(random.randint(1, 10))
    return arr


def product_list(arr):
    result_lst = []
    i = 0
    while i < round(len(arr) / 2, 1):
        result_lst.append(arr[i] * arr[-i - 1])
        i += 1
    return result_lst


lst = create_array(5)
print(lst)
print(product_list(lst))
