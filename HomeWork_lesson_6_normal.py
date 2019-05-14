# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать
# в неограниченном кол-ве классов свой определенный предмет.
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class Person:
    def __init__(self, name, surname, birtg_date):
        self.name = name
        self.surname = surname
        self.birtg_date = birtg_date

    def get_full_name(self):
        return self.name + ' ' + self.surname

class Student(Person):
    def __init__(self, name, surname, birtg_date, class_room, mother, father, lesson):
        super().__init__(name, surname, birtg_date)
        self.class_room = class_room
        self.mother = mother
        self.father = father
        self.lesson = lesson
    def get_class(self):
        return self.class_room

class Teacher(Person):
    def __init__(self, name, surname, birtg_date, class_room, lesson):
        super().__init__(name, surname, birtg_date)
        self.lesson = lesson
        self.class_room = class_room

students = [Student('Alex', 'Moskotlinov', '02.12.2014', '5 A', 'Roman', 'Tatiana', ['Matematika', 'Geometry']),
            Student('Mikhail', 'Titov', '01.11.2013', '7 B', 'ivan', 'rita', ['Matematika', 'Geometry']),
            Student('Irina', 'ivanova', '03.01.2014', '1 A', 'dmitriy', 'sveta', ['Matematika', 'Geometry']),
            Student('Olesya', 'zaykina', '02.12.2014', '2 B', 'oleg', 'vika', ['Matematika', 'Geometry']),
            Student('Stas', 'zoykin', '04.11.2015', '5 A', 'igor', 'rita', ['Matematika', 'Geometry'])]

for student_all in students:
    print(student_all.get_class())

for student_all in students:
    if student_all.class_room == '5 A':
        print(student_all.get_full_name())

teachers = [Teacher('Ivanov', 'Ivan', '01.01.1954', '2 B', 'Matematika'),
            Teacher('Sidorov', 'Alex', '11.01.1960', '1 A', 'Geometry')]


# student1 = Student('Alex', 'Moskotlinov', '02.12.2014', '1 A', 'Roman', 'Tatiana')
# teacher1 = Teacher('Ivanov', 'Ivan', '01.01.1954', '2 B', 'Matematika')


# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе