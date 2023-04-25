# print(11111 * 1111111)


# print(50 // 9)

#print(44 % 5)

# print(42 / (4 + 2 * (-2)))

# print(2014 ** 14)

# print(+ 42)


# print(0.3 + 0.3 + 0.3)

# print(1.2345e3)

# print(1.2345e-3)

#print(2014.0 ** 14)
#print(7 / 3)
#print(7 // 3)

#x = 2.99
#int(x)
#print(int(x))


#x = -1.6
#int(x)
#print(int(x))


#print((9 ** 19) - (int(float(9 ** 19))))


#y = ("")
#print('Hello! What is your name?')
#name = input()
#name = str(name)
#while name == y:
 #   print('Sorry! Enter your name.')
 #   name = input()
 #   name = str(name)
#else:
 #   print('Nice to meet you,', name, '.', 'How old are you?')
#old = input()
#old = int(old)
#if old == 18:
 #   print('Welcome')
#elif old > 18:
 #   print('Welcome')
#else:
 #   print ('You are too young, bye!')



#X = int(input())
#print(X // 60)
#print(X % 60)


#X = int(input())
#H = int(input())
#M = int(input())
#Y = (X + (H * 60) + M)
#print(Y // 60)
#print(Y % 60)

#x = 5
#y = 10
#print (y > x * x or y >= 2 * x and x < y)

#a = True
#b = False
#print (a and b or not a and not b)


#a = int(input())
#b = int(input())
#h = int(input())
#if h < a:
 #   print('Недосып')
#elif h > b:
 #   print('Пересып')
#else:
 #   print('Это нормально')


#year = int(input())
#if year % 4 == 0 and year % 100 != 0:
 #    print('Високосный')
#elif year % 400 == 0:
#    print('Високосный')
#else:
 #   print('Обычный')




#print ("123" + "42")



#a = int(input())
#b = int(input())
#c = int(input())

#p = (a + b + c) / 2

#S = (p * (p - a)) * (p - b) * (p - c)

#sqrt = S ** (0.5)
#print (sqrt)



'''
num = int(input())

if num > -15 and num <= 12:
    print('True')
elif num > 14 and num <17:
    print('True')
elif num >= 19:
    print('True')
else:
    print('False')
'''


""""
num1 = float(input())
num2 = float(input())
oper = input()

if oper == '+':     # сложение
    x1 = num1 + num2
    print(x1)
elif oper == '-':     # вычитание
    x1 = num1 - num2
    print(x1)
elif oper == '/':       # деление
    if num2 == 0:
        print('Деление на 0!')
    else:
        x1 = num1 / num2
        print(x1)
elif oper == '*':       # умножение
    x1 = num1 * num2
    print(x1)
elif oper == 'mod':     # остаток от деления
    if num2 == 0:
        print('Деление на 0!')
    else:
        x1 = num1 % num2
        print(x1)
elif oper == 'div':     # целочисленное деление
    if num2 == 0:
        print('Деление на 0!')
    else:
        x1 = num1 // num2
        print(x1)
elif oper == 'pow':     # возведение в степень
    x1 = num1 ** num2
    print(x1)
"""

""""
type = input()
pi = 3.14
if type == 'треугольник':
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = ((p * (p - a)) * (p - b) * (p - c)) ** 0.5
    print(S)
elif type == 'прямоугольник':
    a = float(input())
    b = float(input())
    S = a * b
    print(S)
elif type == 'круг':
    r = float(input())
    S = pi * r ** 2
    print(S)
"""


"""
x1 = int(input())
x2 = int(input())
x3 = int(input())

X = x1, x2, x3
minx = min(X)
maxx = max(X)

sumx = x1+x2+x3
avgx = sumx - minx - maxx

print(maxx, minx, avgx, sep="\n")
"""

"""
X = list(input())

x1 = X[0]
x2 = X[1]
x3 = X[2]
x4 = X[3]
x5 = X[4]
x6 = X[5]

x = int(x1) + int(x2) + int(x3)
y = int(x4) + int(x5) + int(x6)

if x == y:
    print('Счастливый')
else:
    print('Обычный')
"""


"""
i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
    print(i)
"""

"""
print('Hello! What is your name?')
name = input()
while name == '' or '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in name:
    if name == '':
        print('Sorry! Enter your name.')
        name = input()
    elif '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' in name:
        print('Sorry! The name cannot contain numbers. Enter your name.')
        name = input()
else:
    print('Nice to meet you,', name, '.', 'How old are you?')
old = input()
old = int(old)
if old == 18:
    print('Welcome')
elif old > 18:
    print('Welcome')
else:
    print ('You are too young, bye!')
"""

'''
x = int(input())

y = x % 10

if x % 100 == 11 or x % 100 == 12 or x % 100 == 13 or x % 100 == 14:
    print(x, 'программистов')
else:
    if x == 0 or x >= 5 and x <= 20 or y > 4 and y <= 9 or y == 0:
        print(x, 'программистов')
    elif x == 1 or y == 1:
        print(x, 'программист')
    elif x >= 2 and x <= 4 or y == 2 or y == 3 or y == 4:
        print(x, 'программиста')
'''

'''
x = int(input())

s = 0

while x != 0:
    s += x
    x = int(input())
else:
    print(s)
'''


"""
a = int(input())
b = int(input())

x = min(a, b)
d = x

while d % a != d % b:
    d += 1
else:
    print(d)
"""

"""
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        break
    i = i + 1
print(i)
"""

"""
i = 0
s = 0
while i < 10:
    i = i + 1
    s = s + i
    if s > 15:
        continue
    i = i + 1
print(i)
"""

"""
i = 0

while i >= 0:
    x = int(input())
    if x <= 100 and x >= 10:
        print(x)
        i += 1
    if x > 100:
        break
    if x < 10:
        continue
"""

"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for x in range(c, d + 1):
    print('\t', x, end='')
print()
for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i*j, '\t', end='')
    print()
"""

"""
a = int(input())
b = int(input())
s = 0
n = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        s += i
        n += 1
x = s / n
print(x)
"""

"""
x = str(input())
y = x.upper()
sum = len(x)
s = 0
for i in y:
    if i == 'C' or i == 'G':
        s += 1
print(float((s/sum)*100))
"""

"""
s = 'abcdefghijk'
s1 = s[3:6]
s2 = s[:6]
s3 = s[3:]
s4 = s[::-1]
s5 = s[-3:]
s6 = s[:-6]
s7 = s[-1:-10:-2]
print(s1, s2, s3, s4, s5, s6, s7, sep='\n')
"""

"""
s = str(input()) + ''
j = 1
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        j += 1
    else:
        print(s[i], j)
        j = 1
"""

"""
s = input()
counter = 0
counter1 = 0
y = len(s)
while y != 0:
    for i in range(len(s)):
        if s[0 + counter1] == s[i]:
            counter += 1
            y -= 1
        else:
            counter1 = counter
            continue

print(s[0], counter, sep='')
print(len(s), y, counter1)
"""

"""
s = input()
counter = 1
x = []
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        counter += 1
    elif s[i] != s[i + 1]:
        x.append(s[i] + str(counter))
        counter = 1
print(*x, s[len(s) - 1], counter, sep='')
"""

"""
a = [1, 2, 3]
b = a
# значения списка b?
print(a, b, sep='\n')
a[1] = 10
# значения списка b?
print(a, b, sep='\n')
b[0] = 20
# значения списка a?
print(a, b, sep='\n')
a = [5, 6]
# значения списка b?
print(a, b, sep='\n')
"""

"""
s = [int(i) for i in input().split()]
print(sum(s))
"""

"""
s = input().split()
x = []
if len(s) > 1:
    for i in range(len(s) - 1):
        x.append(int(s[i - 1]) + int(s[i + 1]))
    print(*x, int(s[len(s) - 2]) + int(s[0]))
else:
    print(int(s[0]))
"""

"""
s = [int(i) for i in input().split()]
s.sort()
counter = 1
x = []
if len(s) > 1:
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            counter += 1
        elif s[i] != s[i + 1]:
            if counter > 1:
                x.append(s[i])
            else:
                continue
            counter = 1
    if s[i] == s[len(s) - 1]:
        print(*x, s[i])
    else:
        print(*x)
else:
    print()
"""

"""
from random import *
from math import log2, ceil

num1, num2 = int(input()), int(input())
rand_num = randint(num1, num2)
sum_attempts = ceil(log2(num2 - num1)) + ceil((num2 - num1) / 100 * 5)
if sum_attempts == 1 or (sum_attempts // 10 > 1 and sum_attempts % 10 == 1):
    print('У тебя будет', sum_attempts, 'попытка')
elif 2 <= sum_attempts <= 4 or (sum_attempts // 10 > 1 and sum_attempts % 10 in (2, 3, 4)):
    print('У тебя будет', sum_attempts, 'попытки')
else:
    print('У тебя будет', sum_attempts, 'попыток')
"""

"""
flag = True
x = 0
n = []
while flag == True:
    y = int(input())
    n.append(y)
    x += y
    if x == 0:
        flag = False
sum_sqrt = 0
for i in n:
    sum_sqrt += i**2

print(sum_sqrt)
"""

"""
n = int(input())
counter = 0
for i in range(1, n + 1):
    if counter == n:
        break
    for j in range(i):
        print(i, end=' ')
        counter += 1
        if counter == n:
            break
"""

"""
n = [int(i) for i in input().split()]
x = int(input())
s = []
for i in range(len(n)):
    if x == n[i]:
        s.append(i)
if len(s) == 0:
    print('Отсутствует')
else:
    print(*s)
"""

"""
def f(x):
    if x <= -2:
        return 1 - (x + 2)**2
    elif -2 < x <= 2:
        return -(x / 2)
    elif 2 < x:
        return (x - 2)**2 + 1

#print(f(float(input())))
"""

"""
def modify_list(s):
    for i in reversed(range(len(s))):
        if s[i] % 2 != 0:
            s.remove(s[i])
        elif s[i] % 2 == 0:
            x = s[i] // 2
            s.pop(i)
            s.insert(i, x)
s = [int(i) for i in input().split()]
modify_list(s)
#print(s)
"""

"""
def update_dictionary(d, key, value):
    pass

d = {}
"""

"""
s = [i.lower() for i in input().split()]
d = {}
for i in s:
    d[i] = s.count(i)
for key, value in d.items():
    print(key, value)
"""

"""
d = {}
n = int(input())
for i in range(n):
    x = int(input())
    if x in d:
        print(d[x])
    else:
        d[x] = f(x)
        print(d[x])
"""

with open ('C:\\Users\\strel\\OneDrive\\Рабочий стол\\dataset_3363_2 (1).txt', 'r') as inf:
    s = inf.read()
num = []
abc = []
for i in s:
    if i.isdigit():
        num.append(int(i))
    elif i.isalpha():
        abc.append(i)
x = ''
for i in range(len(abc)):
    x += abc[i] * num[i]

with open ('C:\\Users\\strel\\OneDrive\\Рабочий стол\\dataset_3363_2 (1).txt', 'w') as inf:
   inf.write(str(x))