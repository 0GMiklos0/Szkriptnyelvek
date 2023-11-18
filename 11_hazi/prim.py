#!/usr/bin/env python3
import json

def main():
    with open("primes.json","w") as f:
        primnums = [True for i in range(10000001)]
        
        print(primnums)
if __name__ == "__main__":
    main()