'''Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6
'''

# a = 8
# f1 = 0
# f2 = 1
# f3 = 0
# i = 2
# while f3 < a:
#     f3 = f1 + f2
#     f1 = f2
#     f2 = f3
#     i += 1
#     print(f3, i)
#     if f3 > a: i = -1

# print(i)


# count = 5

# num = int(input())
# max1=num
# min1=num

# while count>1:
    
#     num = int(input())
#     if num>max1:
#         max1=num
#     if num<min1:
#         min1=num
#     count-=1
# print(max1,min1)

n = [0, 1, 0, 1, 0, 0]
i = 0
count0 = 0
count1 = 0
while i < len(n):
    if n[i] == 0: count0 += 1
    else: count1 += 1
    i += 1
# print(count0, count1)
if count0 < count1: print(count0)
else: print(count1)

