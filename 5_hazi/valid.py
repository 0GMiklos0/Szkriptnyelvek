#!/usr/bin/env python3
def valid(text, chars="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"):
    inside = []
    for s in text:
        if s in chars:
            inside.append(s)
    return ''.join(inside)

def main():
    print(valid('LolXd'))

if __name__ == "__main__":
    main()