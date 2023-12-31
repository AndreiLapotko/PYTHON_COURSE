import random

'''Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''

# вариант решения 2
# n = int(input('Введите количество чисел: '))
# nums = []
# for i in range(n):
#     nums.append(random.randint(-10, 10))
# print(nums)
# nums = [1, 1, 2, 0, -1, 3, 4, 4]
# nums = set(nums)
# # print(nums)
# print(len(nums))

# вариант решения 2
# nums = [1, 1, 2, 0, -1, 3, 4, 4]
# result = []
# for i in nums:
#     if i not in result:
#         result.append(i)
# print(result)
# print(len(result))


'''Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''
# вариант решения 1
# nums = [1, 2, 3, 4, 5]
# k = 2
# print(*nums[-k:], *nums[:-k])

# # вариант решения 2
# while k > 0:
#     temp = nums.pop()
#     nums.insert(0, temp)
#     k -= 1
# print(nums)


'''
Задача №21. Напишите программу для печати всех уникальных значений в словаре. 
Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# thing = set()
# for x in list_1:
# # вариант 1
#     # for y in x:
#     #     thing.add(x[y])

# # вариант 2
#     # for y in x.values():
#     #     thing.add(y)

# # вариант 3
#     for y, z in x.items():
#         thing.add(z)
#         # print(y, z)

# print(thing)


'''
Задача №23. Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3) 
Примечание: Пользователь может вводить значения списка или список задан изначально.'''

n = int(input('Введите количество чисел: '))
nums = []
for i in range(n):
    nums.append(random.randint(-10, 10))
print(nums)

# n = [4, 0, 10, 1, 4]
# n = [7, 8, 3, -8, 6, 2, -2, -6, -10, -1]
result = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]: result += 1
print(result)