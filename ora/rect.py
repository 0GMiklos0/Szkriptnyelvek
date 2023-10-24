#!/usr/bin/env python3
class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.width = width
    def area(self):
        return self.height*self.width
    def __bool__(self):
        return self.area() > 0
    def __lt__(self, other): #less than operator
        return self.area() < other.area()
    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
# destruktor nincs

def main():
    rect = Rectangle(50,10)
    rect.width = 60
    print(rect)

if __name__ == "__main__":
    main()