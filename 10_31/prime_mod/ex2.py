#!/usr/bin/env python3

from pygyak import is_prime

def main():
    fel2 = sum([i for i in range(200) if is_prime(i)])
    print(fel2)
    
if __name__ == "__main__":
    main()