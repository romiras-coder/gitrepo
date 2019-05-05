# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
import os, sys
print("путь - ", sys.argv)

def print_help():
    print("help - справка о програме ")
    print("lsdir - содержимое текущей папки ")
    print("rmdir <dirname> - удалить папку ")
    print("mkdir <dirname> - создать папку ")
    print("cddir <dirname> - перейти в папку ")

def list_dir():
    print(os.listdir(os.getcwd()))

def make_dir():
    if not dir_name:
        print("Необходимо указатьимя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print(f"Директория {dir_name} успешно созданна")
    except FileExistsError:
        print(f"Директория {dir_name} уже существует")

def remove_dir():
    if not dir_name:
        print("Необходимо указатьимя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.rmdir(dir_path)
        print(f"Директория {dir_name} успешно удалена")
    except FileExistsError:
        print(f"Директория {dir_name} не существует")

def change_dir():
    if not dir_name:
        print("Необходимо указатьимя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.chdir(dir_path)
        print(f"Успешный переход впапку {dir_name}")
    except FileExistsError:
        print(f"Директории {dir_name} не существует")
do ={
    "help": print_help,
    "mkdir": make_dir,
    "lsdir": list_dir,
    "rmdir": remove_dir,
    "cddir": change_dir,
    }
try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None
try:
    key = sys.argv[1]
except IndexError:
    key = None
if key:
    if do.get(key):
        do[key]()
    else:
        print("Invalid key, try again (info - help)")