
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка с
# нечетными индексами.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint as rnd
#
# size = (int(input('Введите размер списка: ')))
#
# my_list = []
#
# for i in range(size):
#     my_list.append(rnd(1, 10))
#
# print(my_list)
#
# Sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         Sum += my_list[i]
#
# print(f'Сумма элементов с нечётными индексами = {Sum}')



from random import randint as rnd

size = (int(input('Введите размер списка: ')))

my_list = [rnd(1, 10) for i in range(size)] # list comprehension

print(my_list)

# Sum = 0
# for i in range(len(my_list)):
#     if i % 2 != 0:
#         Sum += my_list[i]

Sum = [lambda i: my_list[i] if i % 2 != 0 else]

print(f'Сумма элементов с нечётными индексами = {Sum}')