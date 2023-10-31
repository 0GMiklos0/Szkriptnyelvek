#!/usr/bin/env python3
def duplaz(n):
    return n*2

def main():
    print([duplaz(i) for i in range(10)])
    
def is_palindrom(n):
    return n.lower() == n.lower()[::-1]

if __name__ == "__main__":
    print(__name__)
    print("3 ketszerese", duplaz(3), "\n6 ketszerese", duplaz(6))