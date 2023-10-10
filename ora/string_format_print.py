#!/usr/bin/env python3

def hello(nev,szin,t):
    nev = nev.capitalize()
    #print("{n} {c} az {o}".format(n = nev, c=szin, o=t))
    #print("{} {} az {}!".format(nev, szin, t))
    #print("{0} {1} az {2}".format(nev, szin, t))
    #print(f"2 + 1 = {2+1}")
    print(f"{nev} {szin} az {t}!")

def main():
    hello("geza","kek","eg")
    hello("boi","boi","boi")
    #slicing
    s = "string"
    print(s[0])
    print(s[0:2])
    print(s[::2])
    print(s[::-1])

if __name__ == "__main__":
    main()