# Последовательностью Фибоначчи называется последовательность чисел a0,
# a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
 
# print(fibonacci(10)) 


# найти фаториал N через рекурсию

# num = 5
# def factorial(num):
#     if num == 0: return 1
#     return num * factorial(num - 1)


# print(factorial(num))


# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. 
# В программе запрещается объявлять массивы и использовать циклы 
# (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

x = 4

def reverse(n):
    if n == 0: return ' '
    a = input("Введите число ")
    return reverse(n - 1) + a


print(reverse(x))