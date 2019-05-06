import os
def do_something():
    return "I'm func do_something in module lib1"

def more_then_one(num):
    return num > 1

def listt_dir():
    return os.listdir(os.getcwd())


# import os
# def make_dirs():
#     return os.mkdir()


# for i in range(1, 10):
#     dname = os.path.join(os.getcwd(), "dir_{}".format(str(i)))
#     os.mkdir(dname)
#     print("Директория {} успешно создана".format(dname))
#     try:
#         os.mkdir(dname)
#     except FileExistsError:
#         print('Такая директория уже существует')