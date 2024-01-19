'''
задается строка из цифр '2 4 -23 5 13 897 11'
'''

# str01 = '2 4 -23 5 13 897 11'

# res = list(filter(lambda int(x): abs(x) > 9, str01.split()))

num = '2 4 -23 5 13 897 11'
print(*list(filter(lambda x: len(x.replace('-','')) == 2, num.split())))
print(*list(filter(lambda x: 9 < abs(int(x)) < 100, num.split())))
print(*list(filter(lambda x: len(str(abs(int(x)))) == 2, num.split())))


