#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély","hhh"]
    mely = False
    magas = False
    for s in words:
        for ch in s:
            if ch in MELY_MGHK:
                mely = True
            if ch in MAGAS_MGHK:
                magas = True
        if mely & magas:
            print(s, "vegyes")
        elif mely:
            print(s, "mely")
        elif magas:
            print(s, "magas")
        else:
            print(s, "egyik sem")
        mely, magas = False, False
        

if __name__ == "__main__":
    main()