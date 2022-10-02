# Реализуйте алгоритм перемешивания списка.
# Список размерностью 10 задается случайными целыми числами, выводится на экран,
# затем перемешивается, опять выводится на экран. SHUFFLE нельзя юзать!
import random

array = []
for i in range(10):
    array.append(random.randint(1, 10))
print(array)


def mix_array(array):
    array.reverse()
    result_array = array
    m = len(result_array)
    while (m):
        m -= 1
        i = random.randint(0, m)
        result_array[m], result_array[i] = result_array[i], result_array[m]
    return result_array
print("mix:")
print(mix_array(array))
