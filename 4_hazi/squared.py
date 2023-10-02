#!/usr/bin/env python3

def main():
    a = sum([i**2 for i in range(101)])
    b = sum(range(101))**2 
    print(b - a)

if __name__ == "__main__":
    main()