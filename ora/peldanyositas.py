#!/usr/bin/env python3
class Peldany:
    peldany = 0
    def __init__(self):
        Peldany.peldany += 1
    
    @staticmethod
    def peldanyszam(): # osztalymetodus (nincs self)
        return Peldany.peldany
    
    @classmethod
    def pldnyszm(cls): # oroklesnel van lenyeges kulonbseg
        return Peldany.peldany

def main():
    p1 = Peldany()
    p2 = Peldany()
    p3 = Peldany()
    p4 = Peldany()
    p5 = Peldany()
    print(Peldany.peldany)

if __name__ == "__main__":
    main()