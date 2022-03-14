class Student:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


student = Student("Ali", 20, "Baghdad")
print(student.name, student.age, student.city)


class Polygon:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides


triangle = Polygon("Triangle", 3)
square = Polygon("Square", 4)
pentagon = Polygon("Pentagon", 5)
hexagon = Polygon("Hexagon", 6)

print(triangle.name, triangle.sides)
print(square.name, square.sides)
print(pentagon.name, pentagon.sides)
print(hexagon.name, hexagon.sides)


