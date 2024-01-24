# Заполните массив элементами арифметической прогрессии. Её первый элемент a1 , 
# разность d и количество элементов n будет задано автоматически. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

n = int(input())
a1 = int(input())
d = int(input())
arr = []
 
for i in range(n):
    c = a1 + i*d
    arr.append(c)
 
# Вторая
import random
 
arr = [random.randint(20,100) for i in range(100)]
evens = 0
unevens = 0
for c in arr:
    if c%2 == 0:
        evens += 1
    else:
        unevens += 1