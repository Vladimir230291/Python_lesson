# Задайте натуральное число Напишите программу,которая составит список простых множителей числа N.

try:
    n = int(input("Введите число: "))
    while n > 1:
        i = 2
        f = 0
        while True:
            if n % i == 0:
                n //= i
                print(i, end=" ")
                f = 1
                break
            else:
                i += 1
        if f == 1:
            continue
except:
    print("Введите натуральное число")


