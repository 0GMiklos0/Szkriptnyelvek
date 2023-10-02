import sys
import random as r

UPTO = 100


def main():
    li = []
    for i in range(UPTO):
        if len(li) < 10:
            rand = r.randint(0, 9)
            li.append(str(rand))
        else:
            print(''.join(li))
            li = []

if __name__ == "__main__":
    main()