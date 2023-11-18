#!/usr/bin/env python3
import re

def main():
    with open("11_hazi/corpus.txt", "r") as f:
        li = f.read().splitlines()
        properwords = []
        for i in li:
            if re.search(".*j.*s.*u.*n.*", i):
                properwords.append(i)
        print(properwords)
        
if __name__ == "__main__":
    main()