# Задайте два числа.Напишите программу, которая
# найдёт НОК(наименьшее общее кратное) этих двух чисел.
try:
    a, b = map(int, input("Введите 2 числа через пробел: ").split())

    i = min(a, b)
    while True:
        if i % a == 0 and i % b == 0:
            break
        i += 1
    print("Наименьшее общее кратное: ", i)
except:
    print("Ошибка")