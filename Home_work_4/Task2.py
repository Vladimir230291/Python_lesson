# Задайте последовательность чисел.Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.
try:
    lst = list(map(int, input("Введите числа через пробел: ").split()))
    print(lst)
    result_list = []
    for i in lst:
        if i not in result_list:
            result_list.append(i)
    print(result_list)
except:
    print("Введите числа через пробел!")


