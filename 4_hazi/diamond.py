#!/usr/bin/env python3
import string
import math

def diamond(num):
    if num%2 == 0:
        print("Nem helyes a megadott szam, adjon egy paratlan szamot")
    else:
        for i in range(num):
            star = '*'
            if i < math.ceil(num/2):
                print(((2*i+1)*star).center(num))
            else:
                print(((2*num-(2*i+1))*star).center(num))
            
            

def main():
    diamond(5)

if __name__ == "__main__":
    main()