# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


import os, sys
from shutil import copyfile

print("путь - ", sys.argv)

def print_help():
    print("help - справка о програме ")
    print("lsdir - содержимое текущей папки ")
    print("rmdir <dirname> - удалить папку ")
    print("mkdir <dirname> - создать папку ")
    print("cddir <dirname> - перейти в папку ")
    print("cpdir <dirname> <newdirname> - копировать папку/файл ")

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

def cp_file():
    if not dir_name:
        print("Необходимо указатьимя директории")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        copyfile(sys.argv[2], sys.argv[3])
        print(f"Успешный переход впапку {dir_name}")
    except FileExistsError:
        print(f"Директории {dir_name} не существует")

do ={
    "help": print_help,
    "mkdir": make_dir,
    "lsdir": list_dir,
    "rmdir": remove_dir,
    "cddir": change_dir,
    "cpdir": cp_file,
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