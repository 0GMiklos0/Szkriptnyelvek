from enum import *

class Hangnem(Enum):
    MELY_MGHK = 'aáoóuú'
    MAGAS_MGHK = 'eéiíöőüű'
    def __init__(self, s):
        self.word = s
    def check(self):
        ismely = False
        ismagas = False
        for c in self.word:
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