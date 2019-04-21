__author__ = 'Москотлинов Р.И.'
otstup = 70
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
print("Задача - 1")
print("")


print("_" * otstup)
# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
print("Задача - 2")
print("")
#user_date_1 = input("введите дату в формате dd.mm.yyyy : ")
user_date_1 = "01.12.2013"
date_month = {"01": "Января", "02": "Феараля", "03": "Марта", "04": "Апреля", "05": "Мая", "06": "Июня", "07": "Июля", "08": "Августа", "09": "Сентября", "10": "Октября", "11": "Ноября", "12": "Декабря"}
date_int = {"01": "Первое", "02": "Второе", "03": "Третье", "04": "Четвертое", "05": "Пятое", "06": "Шестое", "07": "Седьмое", "08": "Восьмое", "09": "Девятое", "10": "Десятое", "11": "Одинадцатое", "12": "Двенадцатое", "13": "Тринадцатое", "14": "Четырнадцатое", "15": "Пятнадцатое", "17": "Семнадцатое", "18": "Восемнадцатое", "19": "Девятнадцатое", "20": "Двадцатое", "21": "Двадцать первое", "22": "Двадцать второе", "23": "Двадцатьтретье", "24": "Двадцать четвертое", "25": "Двадцать пятое", "26": "Двадцать шестое", "27": "Двадцать седьмое", "28": "Двадцать восьмое", "29": "Двадцать девятое", "30": "Тридцатое", "31": "Тридцать первое"}
date_all = []
print("Дата: ", user_date_1[0:2])
print("Месяц: ", user_date_1[3:5])
print("Год: ", user_date_1[6::])

for a in date_int:
    if user_date_1[0:2] == a:
       date_all.append(date_int[a])

for b in date_month:
    if user_date_1[3:5] == b:
        date_all.append(date_month[b])

date_all.append(user_date_1[6::])
print(date_all[0] + " " + date_all[1] + " " + date_all[2] + " " +"года")
print("_" * otstup)

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
print("Задача - 3")
print("")

import random
L = [i for i in range(-100, 101)]
print(len(L), sorted(L))
print("_" * otstup)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
print("Задача - 4")
print("")

lst = [1, 2, 4, 5, 6, 2, 5, 2]
#lst2 = set(lst)
lst2 = []

print("Список: ", lst)
#print("Преобразовали списки в множество, только уникальные значения: ", set(lst))
# for n in lst:
#     if n not in lst2:
#         lst2.append(n)
#         #print(lst2)
# print("Преобразовали списки, только уникальные значения: ", lst2)

for m in lst:
    if  m :
        print(m)
        lst2.append(m)

print("Преобразовали списки, только уникальные значения: ", lst2)


print("_" * otstup)