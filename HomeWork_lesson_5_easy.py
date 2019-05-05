# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
print("Задача-1")
import os
print('os.name = ', os.name)
def make_dirs():
    for i in range(1, 10):
        dname = os.path.join(os.getcwd(), "dir_{}".format(str(i)))
        os.mkdir(dname)
        print("Директория {} успешно создана".format(dname))
    try:
        os.mkdir(dname)
    except FileExistsError:
        print('Такая директория уже существует')
make_dirs()

def remove_dirs():
    for i in range(1, 10):
        dname = os.path.join(os.getcwd(), "dir_{}".format(str(i)))
        os.rmdir(dname)
        print("Директория {} успешно удалена".format(dname))
    try:
        os.rmdir(dname)
    except FileExistsError:
        print('Такой директории не существует')
remove_dirs()
print('_' * 50)

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
print("Задача-2")
import os
print(os.listdir(os.getcwd()))
print('_' * 50)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

print("Задача-3")
import os
import sys
from shutil import copyfile
import inspect
# print(os.path.abspath(os.path.dirname(inspect.stack()[0][1]))) # текущая директория
# print(os.path.abspath(inspect.stack()[0][1])) # полный путь до исп файла
# print(os.path.realpath(inspect.stack()[0][1]))
# print(sys.argv)

# newfile = sys.argv[0]
# print(newfile)
# print('sys.argv[0] =', sys.argv[0])
# pathname = os.path.dirname(sys.argv[0])
# print('path =', pathname)
# print('full path =', os.path.abspath(pathname))

copyfile(sys.argv[0], sys.argv[0] + '.bkp')
print()
print('_' * 50)