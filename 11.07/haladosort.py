def mysort(li):
    return li[-1]
def mysort2(s: str):
    return int(s.split(':')[0])*-1
def mysort3(li):
    return li[1]

def main():
    data = [ 
    (1, 'Albany', 'NY', 162692),
    (3, 'Allegany', 'NY', 11986),
    (121, 'Wyoming', 'NY', 8722),
    (123, 'Yates', 'NY', 5094)]
    li = sorted(data, key = mysort)
    print(li)
    users = ['10:User1', '80:User2', '100:User3', '00:User4', '75:User4', '45:User5']
    print(sorted(users, key = mysort2))
    li = [ [2, 6], [1, 3], [5, 4] ]
    print(sorted(li, key=mysort3))
    
main()
    
    