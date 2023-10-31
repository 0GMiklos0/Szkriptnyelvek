import random as r

def shuffled(li):
    changer = li
    r.shuffle(changer)
    return changer[r.randrange(0,len(changer))]

def main():
    r.randint(4,8)
    r.randrange(4,8)
    li = [i for i in range(21)]
    for i in range(10):
        r.shuffle(li)
        print(li)
    
main()