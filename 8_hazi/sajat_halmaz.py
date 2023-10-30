class Verem():
    def __init__(self):
        self.container = []
    def __str__(self):
        nums = ' '.join([str(i) for i in self.container])
        return f"[{nums}"
    def betesz(self, num):
        self.container.append(num)
        return num
    def kivesz(self):
        return self.container.pop()
    
class Sor():
    def __init__(self):
        self.container = []
    def __str__(self):
        nums = ' '.join([str(i) for i in self.container])
        return f"[{nums}"
    def betesz(self, num):
        self.container.append(num)
        return num
    def kivesz(self):
        ri = self.container[0]
        self.container.remove(self.container[0])
        return ri

def main():
    v = Verem()
    v.betesz(10)
    print(v)
    x = v.kivesz()
    print(x)
    s = Sor()
    s.betesz(10)
    print(s)
    xx = s.kivesz()
    print(xx)

if __name__ == "__main__":
    main()
    
