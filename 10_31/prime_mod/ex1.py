#!/usr/bin/env python3

from pygyak import is_prime
#import pygyak

def main():
    fel1 = [i for i in range(100) if is_prime(i)]
    #fel2 = [i for i in range(100) if pygyak.is_prime(i)]
    print(fel1)
    
if __name__ == "__main__":
    main()