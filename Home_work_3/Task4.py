# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

try:
    num = int(input("Введите число "))
    result = ""
    while num > 0:
        result = str(num % 2) + result
        num //= 2

    print(result)
except:
    print("Введите целое число")



