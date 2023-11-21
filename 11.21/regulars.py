#!/usr/bin/env python3
import re

def Find(pat, text):
    match = re.search(pat, text)
    if match:
        print(match.group())
    else:
        print("nincs benne")

def main():
    Find(r"[a-z0-9_.]+@[a-z0-9_.]+", "asdasdasdasdasd.com")
    
if __name__ == "__main__":
    main()