def oszlop(li):
    return li[1]

def my(t):
    return t[-1]

def id(s : str) -> int:
    t = s.split(":")
    s = t[0]
    #print(s)
    return int(s) * -1
    
def main():
    data = [(1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)]
    print(sorted(data, key=my))

    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(users, key=id))
    li=[ [2, 6], [1, 3], [5, 4] ]
    print(sorted(li, key=oszlop))

if __name__=="__main__":
    main()