'''
Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2 
'''
'''
n = int(input('Введите число n монеток: '))
from random import randint
a, b = 0, 0
for i in range(n):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0: a += 1
    else: b += 1
    print()
if a > b:
    print(f'нужно перевернуть {b} монеток')    
else:
    print(f'Нужно перевернуть {a} монеток') 
'''    

s = int(input('Введите сумму числе: '))
p = int(input('Введите произведение: '))
a = 0
for x in range(s):
    for y in range(s):
        if x + y == s and x * y == p:
            a += 1
            print(x, end=' ')

'''
n = int(input('Введите число N: '))
k = 0
res = 1
while res < n+1:
    print(res, end=' ')
    k += 1
    res = 2 ** k
'''