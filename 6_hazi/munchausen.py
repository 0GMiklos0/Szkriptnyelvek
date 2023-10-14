#!/usr/bin/env python3
def munchausen(num):
    li = [int(s)**int(s) for s in str(num)]
    if sum(li) == num:
        return True

def main():
    limun = []
    for i in range(44000000):
        if munchausen(i):
            limun.append(i)
            print(i)
        else:
            print(i)
    print(limun)

if __name__ == "__main__":
    main()