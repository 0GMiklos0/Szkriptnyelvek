#!/usr/bin/env python3
def mysorted(li):
    newli = li.copy()
    newli.sort()
    return newli
    
def main():
    li = [i for i in range(10)]
    li.append(2)
    print(mysorted(li),li)
    
if __name__ == "__main__":
    main()