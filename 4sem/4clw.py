# ; На вход программе подаются две строки текста, 
# ; содержащие по одному слову из перечня 
# ; "камень", "ножницы", "бумага", "ящерица" или "Спок". 
# ; На первой строке записан выбор Тимура, на второй – выбор Руслана.

# ; Формат выходных данных
# ; Программа должна вывести результат жеребьёвки: 
# ; кто победил - Тимур или Руслан, или они сыграли вничью.

# ; Примечание. Правила игры стандартные:

# ; ножницы режут бумагу. 
# ; Бумага заворачивает камень.
# ; Камень давит ящерицу, а ящерица травит Спока, 
# ; в то время как Спок ломает ножницы, которые, в свою очередь, 
# ; отрезают голову ящерице, которая ест бумагу, 
# ; на которой улики против Спока. Спок испаряет камень, 
# ; а камень, разумеется, затупляет ножницы.

# from pickletools import string1

# a=input()
# b=(input)
# m = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
# 'камень-ящерица': 'Тимур', 'камень-Спок': 'Руслан', 'ножницы-ножницы': 'ничья',
# 'ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан', 'ножницы-ящерица': 'Тимур',
# 'ножницы-Спок': 'Руслан', 'бумага-бумага': 'ничья', 'бумага-камень': 'Тимур',
# 'бумага-ножницы': 'Руслан', 'бумага-ящерица': 'Руслан', 'бумага-Спок': 'Руслан',
# 'ящерица-ящерица': 'ничья', 'ящерица-Спок': 'Тимур', 'ящерица-ножницы': 'Руслан',
# 'ящерица-бумага': 'Тимур', 'ящерица-камень': 'Руслан', 'Спок-Спок': 'ничья',
# 'Спок-ножницы': 'Тимур', 'Спок-бамага': 'Руслан', 'Спок-камень': 'Тимур',
# 'Спок-ящерица': 'Руслан'}

# string1 = a + '-' + b
# print(m[string1])

# ; Пользователь вводит текст(строка). Словом считается последовательность
# ; непробельных символов идущих подряд, слова разделены одним или большим числом пробелов. 
# ; Определите, сколько различных слов содержится в этом тексте.

# input = "She sells sea shells on the sea shore The shells that   \
#  she sells are sea shells I'm sure.So if she sells sea shells on \
#   the sea shore I'm sure that the shells are sea shore           \
#    shells".replace('.', ' ').upper().split()
# str = set(input)
# print(input)

# print(len(str))


# Задача No25. Решение в группах
# Напишите программу, которая принимает на вход строку, и отслеживает, 
# сколько раз каждый символ уже встречался. Количество повторов
# добавляется к символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

word = 'a a a b c a a d c d d'.split()
result = {}
for i in word:
    if i not in result:
        print(i, end = " ")
        result[i] = 1
    else:
        print(f"{i}_{result[i]}", end = " ")    
        result[i] += 1
  


# Вводятся номера телефонов в одну строчку через пробел с разными кодами
# стран: +7, +6, +2, +4 и т.д. Необходимо составить словарь d, где ключи
# - это коды +7, +6, +2 и т.п., а значения - список номеров
# (следующих в том же порядке, что и во входной строке)
# с соответствующими кодами. Полученный словарь вывести командой:

# print(*sorted(d.items()))

# Sample Input:
# +71234567890 +71234567854 +61234576890 +52134567890 +21235777890
# +21234567110 +71232267890
# Sample Output:
# ('+2', ['+21235777890', '+21234567110']) ('+5', ['+52134567890']) 
#('+6', ['+61234576890']) ('+7', ['+71234567890', '+71234567854','+71232267890'])