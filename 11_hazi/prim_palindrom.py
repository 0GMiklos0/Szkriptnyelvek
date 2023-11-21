#!/usr/bin/env python3

import json

def main():
    with open("primes.json", "r") as f:
        li = list(json.load(f))
        li = [i for i in li if str(i) == str(i)[::-1]]
        print(li)
if __name__ == "__main__":
    main()