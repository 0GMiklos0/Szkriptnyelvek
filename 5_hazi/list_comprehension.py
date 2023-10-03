#!/usr/bin/env python3
import random as r

def main():
    nagybetu = [s.upper() + '!' for s in ["auto", "villamos", "metro"]]
    print(nagybetu)
    kezdobetu = [s.capitalize() for s in ["aladar", "bela", "cecil"]]
    print(kezdobetu)
    nulla = [0 for i in range(10)]
    print(nulla)
    ketszer = [i*2 for i in range(1,11)]
    print(ketszer)
    toint = [int(s) for s in [str(i) for i in range(1,11)]]
    print(toint, [str(i) for i in range(1,11)])
    st = ''.join([str(i) for i in range(1,8)])
    toint2 = [int(s) for s in list(st)]
    print(toint2)
    st2 = "The quick brown fox jumps over the lazy dog"
    length = [len(s) for s in st2.split(' ')]
    print(length)
    st3 = "python is an awesome language"
    first = [s[0] for s in st3.split(' ')]
    print(first)
    comb = [(s, len(s)) for s in st2.split(' ')]
    print(comb)
    underten = [i for i in range(10) if i%2 == 0]
    print(underten)
    squared = [i**2 for i in range(20) if i%2 == 0]
    print(squared)
    squared2 = [i**2 for i in range(20) if i**2%10 == 4]
    print(squared2)
    abc = ''.join([chr(i) for i in range(65,91)])
    print(abc)
    stripper = [s.strip() for s in [' apple ',' banana ',' kiwi ']]
    print(stripper)
    li = [1, 0, 1, 1, 0, 1, 0, 0]
    numstr = ''.join([str(i) for i in li])
    print(numstr)
    
    
if __name__ == "__main__":
    main()