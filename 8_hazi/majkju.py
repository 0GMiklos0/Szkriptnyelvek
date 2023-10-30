class MyQueue():
    def __init__(self):
        self.cont = []
        self.contrev = []
    def append(self, num):
        self.cont.append(num)
    def pop_left(self):
        n = len(self.cont)
        for i in range(n):
            self.contrev.append(self.cont.pop())
        num = self.contrev.pop()
        n = len(self.contrev)
        for i in range(n):
            self.cont.append(self.contrev.pop())
        return num
    def size(self):
        return len(self.cont)
    def is_empty(self):
        return bool(self.cont)

def main():
    sor = MyQueue()
    [sor.append(i) for i in range(10)]
    print(sor.pop_left())
if __name__ == "__main__":
    main()