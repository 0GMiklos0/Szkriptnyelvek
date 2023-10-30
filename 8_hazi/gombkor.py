import math

class Sphere():
    def __init__(self, n):
        self.radius = n
    def __lt__(self, o):
        if self.radius < o.radius:
            return True
        else:
            return False
    def __gt__(self, o):
        if self.radius > o.radius:
            return True
        else:
            return False
    def __le__(self, o):
        if self.radius < o.radius:
            return True
        else:
            return False
    def __ge__(self, o):
        if self.radius > o.radius:
            return True
        else:
            return False

class Ellipse():
    def __init__(self, n):
        self.radius = n
    
def main():
    e1 = Sphere(3)
    e2 = Sphere(4)
    print(e1 < e2)

if __name__ == "__main__":
    main()