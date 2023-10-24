#!/usr/bin/env python3
class EmptyClass:
    pass
# alapertelmezetten orokol egy object class-tol

class MyClass(EmptyClass):
    def helllooo(self): #self = this
        print("hello")

def main():
    o = EmptyClass()
    p = MyClass()
    p.helllooo()    # meghivja a helllooo-t p parameterrel(azaz helllooo(p)) 
    #a hatterben, nekunk csak eleg meghivni a peldany metodusat
    
    
    
if __name__ == "__main__":
    main()