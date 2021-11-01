# ## Classes
#
# class Point:
#
#     # Constructor
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point1 = Point(100,220)
# point1.x = 10
# point1.y = 20
#
# point2 = Point(500,600)
# point2.f_name = "Davinder"
# point2.l_name = "Verma"
#
# print(point1.x)
# print(point1.y)

# print(point2.f_name)
# print(point2.l_name)


## Exercise

class Person:

    def name(self, f, l):
        self.f = f
        self.l = l

    def greeting(self):
        print(f"Hello, {self.f} {self.l}")

davinder = Person()

davinder.name("davinder", "verma")

davinder.greeting()
