'''
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо
Пример
На входе:
var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел
На выходе:
3 5
'''
var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

set02 = {i for i in var2.split()}
set03 = {i for i in var3.split()}

print(*sorted(list(set02.intersection(set03))))

# import random

# initialList = '8 5'.split()
# print(initialList)
# list01 = [str(random.randint(1, 11)) for i in range(1, int(initialList[0]) + 1)]
# list02 = [str(random.randint(1, 11)) for i in range(1, int(initialList[1]) + 1)]

# print(list01)
# print(list02)

# set01 = {i for i in list01}
# set02 = {i for i in list02}
# print(set01)
# print(set02)

# result = sorted(list(set01.intersection(set02)))
# # result.sort()
# print(*result)