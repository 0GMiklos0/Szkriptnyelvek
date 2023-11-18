#!/usr/bin/env python3
def alcatraz(n: int):
    li = [0 for i in range(n)]
    for i in range(n):
        for j in range(n):
            if (j+1)%(i+1) == 0:
                li[j] += 1
    li = [i%2 for i in li]
    li2 = [str(i+1) for i in range(n) if li[i] == 1]
    return ''.join(li2)

def main():
    print(alcatraz(600))

if __name__ == "__main__":
    main()