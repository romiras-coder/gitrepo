class ShortInputError(Exception):
    def __init__(self, lengh, atleast):
        Exception.__init__(self)
        self.lengh = lengh
        self.atleast = atleast

    def __str__(self):
        return f"ShortInputError: Длина введенной строки - {self.lengh};"\
               f"Ожидалось как минимум {self.atleast}"
def max_char(text):
    if len(text) < 2:
        raise ShortInputError(len(text), 2)

try:
    max_char("O")
except ShortInputError as ex:
    print(ex)
else:
    print("Не было исключений")
finally:
    pass

#патерн Bilder
class Bilder:
    def build_body(self):
        raise NotImplementedError()
    def build_lamp(self):
        raise NotImplementedError()
    def build_battery(self):
        raise NotImplementedError()
    def create_flashligtht(self):
        raise NotImplementedError()

class Flashlight:
    def __init__(self, body, lamp, battery):
        self._body = body
        self._lamp = lamp
        self._battery = battery
        self._shine = False

    def on(self):
        self._shine = True
    def off(self):
        self._shine = False
    def __str__(self):
        shine = "on" if self._shine else "off"
        return f'Фонарик [{shine}]'
class Lamp:
    "Лампочка"
class Body:
    "Корпус"
class Battery:
    "Батарейка"

class FlaFlashlightBilder(Bilder):
    def build_body(self):
        return Body()
    def build_lamp(self):
        return Lamp()
    def build_battery(self):
        return Battery()
    def create_flashligtht(self):
        body = self.build_body()
        lamp = self.build_lamp()
        battery = self.build_battery()
        return Flashlight(body, lamp, battery)

builder = FlaFlashlightBilder()
flashlight = builder.create_flashligtht()
flashlight.on()
print(flashlight)

#декораторы

# def my_new_decorator(function_to_decorate):
#     def wrapper_around():
#         print('Код до вызова функции')
#         function_to_decorate()
#         print('Код после вызова функции')
#     return wrapper_around()
#
# @my_new_decorator
# def alone_function():
#     print('Просто функция')
#
# alone_function()

def bread(func):
    def wrippar():
        print('<------>')
        func()
        print('<------>')
    return wrippar

def ingred(func):
    def wrippar():
        print('edferw>')
        func()
        print('werwerwer')
    return wrippar
@bread
@ingred
def sandwich(food = '---hum---'):
    print(food)


#sandwich = bread(ingred(sandwich))
sandwich()


class Wrapper:
    def __init__(self, object):
        self.wrapper = object

    def __getattr__(self, attrname):
        print('Trace: ', attrname)
        return getattr(self.wrapper, attrname)

x = Wrapper([1,2,3,4])
x.pop()
print(x.wrapper)

x = Wrapper({'a':1,'b':2,'v':3,'s':4})
print(x.keys())




