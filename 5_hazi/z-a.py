#!/usr/bin/env python3

def main():
    li = []
    [li.append(chr(i)) for i in range(122,96,-1)]
    print(''.join(li))
    

if __name__ == "__main__":
    main()