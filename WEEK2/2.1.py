def square_area(a): return a*a
def rectangle_area(a,b): return a*b
def triangle_area(b,h): return b*h/2
def circle_area(r): return 3.14*r*r

print("Процедурний:")
print("Square:", square_area(4))
print("Rectangle:", rectangle_area(3,5))
print("Triangle:", triangle_area(6,4))
print("Circle:", circle_area(2))
print("\n")

class Square:
    def __init__(self,a): self.a = a
    def area(self): return self.a*self.a

class Rectangle:
    def __init__(self,a,b): self.a=a; self.b=b
    def area(self): return self.a*self.b

class Triangle:
    def __init__(self,b,h): self.b=b; self.h=h
    def area(self): return self.b*self.h/2

class Circle:
    def __init__(self,r): self.r=r
    def area(self): return 3.14*self.r*self.r

shapes = [Square(4), Rectangle(3,5), Triangle(6,4), Circle(2)]

print("Об'єктно-орієнт:")
for s in shapes:
    print(type(s).__name__, "area =", s.area())