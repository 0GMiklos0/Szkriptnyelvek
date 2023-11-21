#!/usr/bin/env python3
import re

def main():
    with open("11_hazi/corpus.txt", "r") as f:
        li = f.read().splitlines()
        properwords = []
        for i in li:
            c = re.search(r"[a-z]*j[a-z]*s[a-z]*u[a-z]*n[a-z]*", i)
            if c:
                properwords.append(c.group())
        print(properwords)
        
if __name__ == "__main__":
    main()