#!/usr/bin/env python3

def main():
    li = []
    [li.append(chr(i)) for i in range(97,123)]
    ''.join(li)
    

if __name__ == "__main__":
    main()