# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
__author__ = 'Москотлинов Р.И.'

otstup = 70
print("Задача - 1")
print("")

fr = ["яблоко", "банан", "киви", "арбуз"]

for frut in fr:
    print("{}".format(frut))

print("_" * otstup)

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("Задача - 2")
print("")
sp1 = [1, 2, 3, 4, 5]
sp2 = [4, 5, 6, 7, 8]

mn = sp1 + sp2
print("Сложили 2 списка: ", mn)
print("Преобразовали списки в множество: ", set(mn))
print("_" * otstup)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Задача - 3")
print("")
sp_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sp_2 = []
sp_krat =[]
sp_nekrat = []

for found in sp_1:
    if found % 2 == 0:
        sp_krat.append(found)
        sp_2.append(found / 4)
    else:
        sp_nekrat.append(found)
        sp_2.append(found * 2)

print("Исходный список        : ", sp_1)
print("Список кратных чисел   : ", sp_krat)
print("Список не кратных чисел: ", sp_nekrat)
print("Преобразованный список : ", sp_2)
print("_" * otstup)





