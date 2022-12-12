
# Написать программу, которая состоит из 4 этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

# ОРИГИНАЛ
# # этап 1
# from random import randint as rnd
# print('Введите размер списка size: ')
# size = int(input())
#
# rnd_list = []
#
# for i in range(size):
#     rnd_list.append(rnd(1000, 9999))
#
# print(*rnd_list)
#
# # этап 2
# print('Введите цифру, которую хотите удалить: ')
# num_remove = str(input())
#
# for i in range(len(rnd_list)):
#     rnd_list[i] = (str(rnd_list[i])).replace(num_remove, '')
#
# print(*rnd_list)
#
# # этап 3
# sum_list = []
#
# for number in rnd_list:
#     while len(number) > 1:
#         Sum = 0
#         for digit in number:
#             Sum += int(digit)
#             number = str(Sum)
#     else:
#         sum_list.append(number)
#
# print(f'Сумма чисел каждого элемента = {sum_list}')
#
# # этап 4
#
# final_list = []
# for i in sum_list:
#     if i not in final_list:
#         final_list.append(i)
#
# print(f'Финальный массив = {final_list}')


# ИСПОЛЬЗОВАЛА MAP и LIST COMPREHENSION
# этап 1
from random import randint as rnd
size = int(input('Введите размер списка size: '))

rnd_list = [rnd(1000, 9999) for i in range(size)] # list comprehension
print(rnd_list)

# этап 2
num_remove = str(input('Введите цифру, которую хотите удалить: '))

rnd_list = list(map(str, rnd_list)) # map
rnd_list = [rnd_list[i].replace(num_remove, '') for i in range(len(rnd_list))] # list comprehension
print(rnd_list)

# этап 3
def Sum(array: list):
    for number in array:
        while len(number) > 1:
            sum = 0
            for digit in number:
                sum += int(digit)
                number = str(sum)
        else:
            return number

sum_list = list(map(Sum, rnd_list)) # map

print(f'Сумма чисел каждого элемента = {sum_list}')

# этап 4

final_list = set(sum_list) # без использования функций, но зато с использованием множества :)
print(f'Финальный массив = {list(final_list)}')


