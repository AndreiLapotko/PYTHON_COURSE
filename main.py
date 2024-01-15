# def sum_numbers (n):
#     sum01 = 0
#     while n > 0:
#         sum01 += n
#         print(n, sum01)
#         n -= 1
#     return sum01

# print(sum_numbers(5))

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += str(i)
#     return res
# print(sum_str('a', 's', 'd', ' ', 'f'))
# print(sum_str(1, 2, 3, 4))

# import modul01
# print(modul01.max1(10, 15))

# from modul01 import max1
# print(max1(10, 15))

# from modul01 import *
# print(max1(10, 5))

# import modul01 as m01
# print(m01.max1(10, 5))

"""*********************************************************************"""
# def fib(n): # функция возвращает число Фибоначчи
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list1 = []
# for i in range(1, 10):
#     list1.append(fib(i))
# print(list1)

# def quik_sort(array): # функция для быстрой сортировки
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quik_sort(less) + [pivot] + quik_sort(greater)

# print(quik_sort([10, 5, 2]))
"""*********************************************************************"""

# def merg_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merg_sort(left)
#         merg_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list01 = [2,5,4,4,9,2,12,6,7,3,3,10]
# merg_sort(list01)
# print(list01)

"""*********************************************************************"""

# def frame(balls):
#     blz = {
#         'R': 1, # red
#         'Y': 2, # yellow
#         'G': 3, # green (3 points)
#         'Bn': 4, # brown (4 points)
#         'Be': 5, # blue (5 points)
#         'P': 6, # pink (6 points)
#         'Bk': 7, # black (7 points)
#         'W': 0 # white (no points because it's a foul)
#     }
#     if 'W' in balls:
#         return 'Foul'

#     result = 0
#     int_list, str_list = [], []

#     for i in range(len(balls)):
#         if balls[i].isalpha() and balls[i] == 'B':
#             str_list.append(balls[i] + balls[i + 1])
#         elif balls[i].isalpha() and balls[i - 1] == 'B':
#             continue
#         elif balls[i].isalpha():
#             str_list.append(balls[i])

#     for i in range(len(balls)):
#         if balls[i].isalpha() and balls[i] != 'B' and balls[i - len(balls) + 1].isalpha():
#             int_list.append(1)
#         elif balls[i].isdigit() and balls[i - len(balls) + 1].isdigit():
#             int_list.append(int(balls[i] + balls[i + 1]))
#         elif balls[i].isdigit() and balls[i - 1].isdigit():
#             continue
#         elif balls[i].isdigit():
#             int_list.append(int(balls[i]))

#     for i in range(len(str_list)):
#         for x, y in blz.items():
#             if str_list[i] == x:
#                 result += int_list[i] * y

#     if result > 147:
#         return 'invalid data'
#     else:
#         return result

# balls ='R13Bk14YRGBnBkRBeP'

# blz = {
#     'R': 1, # red
#     'Y': 2, # yellow
#     'G': 3, # green (3 points)
#     'Bn': 4, # brown (4 points)
#     'Be': 5, # blue (5 points)
#     'P': 6, # pink (6 points)
#     'Bk': 7, # black (7 points)
#     'W': 0 # white (no points because it's a foul)
# }

# import re # образец
# def frame(balls):
#     if 'W' in balls:
#         return 'Foul'
#     list = re.findall('[A-Z][a-z]*[0-9]*', balls)
#     print(list)
#     sum = 0
#     for ball in list:
#         num = re.findall('[0-9]+', ball)
#         color = ball.rstrip(num[0]) if num else ball
#         print(num, color)
#         n = int(num[0]) if num else 1
#         sum += n * int(blz[color])
#     return sum if sum < 148 else 'invalid data'

# print(frame(balls))

"""*********************************************************************"""
# def create_phone_number(arr):
#     new_arr = [str(i) for i in arr]
#     new_arr.insert(0,'(')
#     new_arr.insert(4,') ')
#     new_arr.insert(8,'-')
#     str01 = ''.join(new_arr)
#     return str01

# # def create_phone_number(n): # образец
# # 	return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# list01 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# print(create_phone_number(list01))

"""*********************************************************************"""
# Your goal in this is to implement a difference function, which subtracts one list from another and returns the result.

# It should remove all values from list a, which are present in list b keeping their order.

# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:

# array_diff([1,2,2,2,3],[2]) == [1,3]


# def array_diff(arr1, arr2):
#     for i in arr2:
#         while i in arr1:
#             arr1.remove(i)
#     return arr1


# print(array_diff([1, 2, 2, 2, 2, 3], [2, 1]))

"""*********************************************************************"""
# def f(x):
#     return x*x

# a = f
# print(f(4))
# print(a(5))

# def summ(a, b):
#     return a + b

# summ = lambda a,b: a + b


# def mult(a, b):
#     return a * b


# def math(op, x, y):
#     print(op(x, y))


# # math(summ, 4, 2)
# math(mult, 4, 5)
# math(lambda a, b: a + b, 11, 4)
# # print(summ(2, 3))

"""*********************************************************************"""
# задача №1
list01 = [1, 2, 3, 5, 8, 15, 23, 38]
# # вариант 1
# list02 = [i for i in list01 if i % 2 == 0]
# list03 = [i * i for i in list02]
# result = list(zip(list02, list03))
# print(list02)
# print(list03)
# print(result)

# # вариант 2
# result = list()
# for i in list01:
#     if i % 2 == 0:
#         result.append((i, i * i))
# print(result)

# вариант 3
# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return [x for x in col if f(x)]

# # res = select(int, list01)
# res = list(map(int, list01))
# print(res)
# # res = where(lambda x: x % 2 == 0, res)
# res = list(filter(lambda x: x % 2 == 0, res))
# print(res)
# # # res = select(lambda x: (x, x * x), res)
# res = list(map(lambda x: (x, x * x), res))
# print(res)
"""*********************************************************************"""
# list_1 = [x for x in range(1, 20)]
# print(list_1)
# list_1 = list(map(lambda x: x * 10, list_1))
# print(list_1)
"""*********************************************************************"""
# data = '15 65 9 88 21 56 3 7 44 21'
# print(data)
# # data = data.split()
# # print(data)
# data = list(map(int, data.split()))
# print(data)
"""*********************************************************************"""

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

"""*********************************************************************"""
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')

# print(57)

# path = 'file.txt'
# data = open(path, 'r')
# for l in data:
#     print(l)
# data.close
