#!/usr/bin/env python3
class ClassWithConstr:
    # a konstruktor: (elvileg az object osztalynak van konstruktora, ami meghivja az init fuggvenyt)
    def __init__(self, name):
        self.name = name
        
    def say_hi(self):
        print("Hi {}!".format(self.name))

def main():
    g = ClassWithConstr("Little Stuart")
    g.say_hi()
    pass

if __name__ == "__main__":
    main()