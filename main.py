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