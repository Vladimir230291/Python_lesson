# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

def create_array(arg):
    array = []
    for i in range(arg):
        array.append(random.randint(1, 20))
    return array

def sum_not_even_elements(arr):
    result = 0
    for i in range(1, len(arr), 2):
        result += arr[i]
    return result

try:
    size = int(input("Введите размер списка: "))
    some_list = create_array(size)
    print(some_list)
    print()
    print(sum_not_even_elements(some_list))
except: print("Введите целое число: ")
