PI = 3.14 #Megallapodas alapjan "konstans"

counter = 0

def f2():
    global counter
    counter = 42
    print('f2: ', counter)

def f1():
    counter = 5
    print('f1: ', counter)
    
def f0():
    print('f0: ', counter)

f0()
f1()
f2()