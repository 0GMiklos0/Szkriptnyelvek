def sakktabla(li):
    li2 = []
    for i in range(7,-1,-1):
        for j in range(8):
            if li[j] == i:
                li2.append(j)
    s = ''
    sor = 0
    for i in range(10):
        oszlop = 0
        for j in range(19):
            if (i == 0 or i == 9) and (j == 0 or j == 18):
                s += '+'
            elif i == 0 or i == 9:
                s += '-'
            elif j == 0 or j == 18:
                s += '|'
            elif j%2 == 1:
                s += ' '
            elif j%2 == 0:
                if li2[sor] == oszlop:
                    s += 'Q'
                else:
                    s += '.'
                oszlop += 1
        s += '\n'
        if i>0:
            sor += 1
    print(s)

def main():
    li = [7,3,0,2,5,1,6,4]
    sakktabla(li)
    li = [0,4,7,5,2,6,1,3]
    sakktabla(li)
    
if __name__ == "__main__":
    main()