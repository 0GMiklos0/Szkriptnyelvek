#!/usr/bin/env python3
from collections import deque

def main():
    a = [1,2,3]
    print(len(a))
    a.append(10)
    print(a)
    a[:2]
    b = a # referencia
    c = a[:] # uj lista
    c == a # osszehasonlitja a ket listat
    for var in a:
        var *= 2
    print(a)
    print(list("wutomg"))
    lista = [10,5,4,7,3,61,2]
    res = []
    for e in lista:
        if e % 2 == 0:
            res.append(e)
    lista.remove(5)
    sor = deque([1,1,3])
    sor.popleft()
    sorted(lista)
    lista.sort()
    max(lista)
    min(lista)
    sum(lista)
    
    
    
if __name__=="__main__":
    main()