# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
#  *Пример:*
#  - 6782 -> 23
# - 0,56 -> 11
a = float(input("Введите число: "))

result = 0
a *= 1000 #Ни чего толкового в голову не пришло кроме как умножить на большое число что бы сдвинуть запятую.
while a > 0:
    result += a % 10
    a /= 10
print(int(result))

