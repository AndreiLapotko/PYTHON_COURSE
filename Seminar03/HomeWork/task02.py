import random
'''Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.

Пример:


list_1 = [1, 2, 3, 4, 5]
k = 6
5
'''

n = int(input('Введите количество элементов: '))
list_1 = []
for i in range(n):
    list_1.append(random.randint(-50, 50))
print(list_1)

# list_1 = [1, 2, 3, 4, 5]
k = 6

# list_1.append(k)
# list_1.sort()
# print(list_1)
# ind = list_1.index(k)
# if ind == len(list_1) - 1: 
#     print(list_1[-2])
# elif list_1[ind] - list_1[ind - 1] < list_1[ind + 1] - list_1[ind]: 
#     print(list_1[ind - 1])
# elif list_1[ind] - list_1[ind - 1] == 0 or list_1[ind + 1] - list_1[ind] == 0:
#     print(list_1[ind])
# else: print(list_1[ind + 1])

min1 = abs(k - list_1[0])
result = list_1[0]
for i in range(1, len(list_1)):
    if abs(k - list_1[i]) < min1: 
        min1 = abs(k - list_1[i])
        result = list_1[i]
print(result)