#!/usr/bin/env python3
def main():
    t1 = "abcdefghijklmnopqrstuvwxyz"
    t2 = t1[2:] + t1[:2]
    t1 += t1.upper()
    t2 += t2.upper()
    print(t1, t2, sep = '\n')
    chr = 'd'
    
    

if __name__ == "__main__":
    main()