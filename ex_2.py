
# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

# ОРИГИНАЛ
# from random import randint as rnd
#
# size = int(input('Введите размер списка: '))
#
# my_list = []
#
# for i in range(size):
#     my_list.append(rnd(1, 10))
#
# print(*my_list)
#
# multipl = []
#
# for i in range(len(my_list)):
#     if i < (len(my_list))/2:
#         multipl.append(my_list[i] * my_list[size - 1])
#     size -= 1
#
# print(*multipl)

# ИСПОЛЬЗОВАЛА LIST COMPREHENSION
from random import randint as rnd

size = int(input('Введите размер списка: '))

my_list = [rnd(1, 10) for i in range(size)] # list comprehension
print(my_list)

center = int(len(my_list)/2) if size % 2 == 0 else int(len(my_list)/2 + 1)
multipl = [my_list[i] * my_list[len(my_list) - 1 - i] for i in range(center)] # list comprehension

print(multipl)