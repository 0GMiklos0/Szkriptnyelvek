#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(word):
    mely = False
    magas = False
    for ch in word:
        if ch in MELY_MGHK:
            mely = True
        if ch in MAGAS_MGHK:
            magas = True
    if mely & magas:
        print(word, "vegyes")
    elif mely:
        print(word, "mely")
    elif magas:
        print(word, "magas")
    else:
        print(word, "egyik sem")

def main():
    words = ["apa", "erkély", "kisvasút", "magas", "mély","hhh"]
    [hangrend(s) for s in words]
        

if __name__ == "__main__":
    main()