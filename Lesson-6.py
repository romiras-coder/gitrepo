class Figure: #родитель
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def info(self):
        print("Figure")
        print("color: " + self.color)

class Rectangle(Figure): # потомок
    def __init__(self, color, width = 100, height = 100):
        super().__init__(color)
        self.width = width
        self.height = height

    def squarre(self):
        return self.width * self.height

    def info(self):
        print("Rectangle")
        print("color: " + self.color)
        print("width: " + str(self.width))
        print("height: " + str(self.height))
        print("squarre: " + str(self.squarre()))

fig1 = Figure("green")
fig1.info()

print()

rect1 = Rectangle("Blue")
print(rect1.info())
print(rect1.squarre())
print()


rect2 = Rectangle("yelow", 1, 3)
print(rect2.get_color())
print(rect2.squarre())

class Tree:
    def __init__(self, kind, height):
        self.kind = kind
        self.height = height
        self.age = 0

    def info(self):
        print(f"{self.age} лет {self.kind}. {self.height} высота дерева")

    def grow(self):
        self.age += 1
        self.height += 0.3
class FrutTree(Tree):
    def __init__(self, kind, height):
        super().__init__(kind, height)

    def give_fruits(self):
        print(f"{self.kind} принесла 40 kg")

tree_1 = Tree("Дую", 0.2)
tree_2 = FrutTree("Яблоня", 0.7)
tree_2.info()
tree_2.grow()
tree_2.info()
tree_2.give_fruits()
tree_1.give_fruits()


class V:
    def _private(self):
        print("Это приватный метод")

v = V()
v._private()


class P:
    def __private(self):
        print("Это приватный метод")

p = P()
p.
