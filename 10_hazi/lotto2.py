import random

def lotto():
    max_kiserlet = 1000000  
    szor = 1
    ossz = 0
    kiserlet = 0
    li = [0, 0, 0, 0, 0, 0]

    while (ossz != 90) and (szor != 996300) and (kiserlet < max_kiserlet):
        szor = 1
        ossz = 0

        for i in range(6):
            li[i] = random.randint(1, 45)
            ossz += li[i]
            szor *= li[i]

        if len(set(li)) == len(li):
            kiserlet += 1
            continue

    if kiserlet < max_kiserlet:
        print("Nyerőszámok:", end=" ")
        for i in range(6):
            print(li[i], end=", ")
    else:
        print("Nem találtam megfelelő kombinációt {} kísérlet után.".format(max_kiserlet))

def main():
    lotto()

if __name__ == "__main__":
    main()
