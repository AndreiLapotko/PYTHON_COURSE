import random

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

# n = [0, 1, 0, 1, 0, 0]
# i = 0
# count0 = 0
# count1 = 0
# while i < len(n):
#     if n[i] == 0: count0 += 1
#     else: count1 += 1
#     i += 1
# # print(count0, count1)
# if count0 < count1: print(count0)
# else: print(count1)

'''Задача №13. Решение в группах Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе. Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50 Input:    6 -> -20 30 -40 50 10 -10 Output: 2'''
n = int(input('Введите количество дней в рассматриваемом периоде: '))
t = []
for i in range(n):
    t.append(random.randint(-10, 50))
print(t)
flag = True
for val in t:
    if val <= 0:
        flag = False
        break
    # print(val)
if flag: print('Это оттепель!')
else: print('Это не оттепель!')