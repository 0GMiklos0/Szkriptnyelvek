#!/usr/bin/env python3
import json

def prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

def main():
    with open("primes.json","w") as f:
        primnums = [i for i in range(2,10000001) if prime(i)]
        json.dump(primnums, f)
if __name__ == "__main__":
    main()