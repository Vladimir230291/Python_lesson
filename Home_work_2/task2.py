# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
try:
    n = int(input("Enter number: "))
    res = 1
    for i in range(1, n):
        res *= i
        print(res, end=" ")
except:
    print("Enter integer number!!")
