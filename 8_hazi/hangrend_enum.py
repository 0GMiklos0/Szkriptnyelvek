from enum import *

class Hangnem(Enum):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'

    def check(w):
        ismely = False
        ismagas = False
        for c in w:
            if c in Hangnem.MELY_MGHK.value:
                ismely = True
            elif c in Hangnem.MAGAS_MGHK.value:
                ismagas = True
        if ismely and ismagas:
            return "vegyes"
        if ismely:
            return "mély"
        if ismagas:
            return "magas"
        else:
            return "semmilyen"




def main():
    [print(Hangnem.check(s)) for s in ["ablak", "erkély", "kisvasút", "magas", "mély"]]

if __name__ == "__main__":
    main()