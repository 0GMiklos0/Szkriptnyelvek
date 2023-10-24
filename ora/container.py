#!/usr/bin/env python3
class Bag:
    def __init__(self):
        self.carriage = []
    def add(self, value):
        self.carriage.append(value)
    def __str__(self):
        return f"Bag({self.carriage})"
    def add_twice(self, val):
        self.add(val)  # igy ha valtozas van az add fuggvenyben, az itt is megvaltozik
        self.add(val)

def main():
    b = Bag()
    b.add(5)
    b.add(7)
    b.add("NEEEEE")
    print(b)
    b.add_twice('boi')
    print(b)

if __name__ == "__main__":
    main()