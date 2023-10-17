import shutil

def read_io():
    f = open("input.txt","r")
    for line in f:
        line = line.rstrip('\n')
        if line.endswith("a"):
            print(line)
    sorok = f.read().splitlines()
    f.close()

def write_io():
    f = open("out.txt","w")
    print("hollo",file=f)
    print("world",file=f)
    print(True, 3.14, "high", 42, sep = "|", file=f)
    
    f.write("aa") # csak string-et fog beleirni, nincs alapertelmezetten sortores
    
    f.close()
    
def open_with_with():
    with open("input.txt","r") as f:
        print(f.read())
        
def copy_2():
    with open("input.txt", "r") as i, open("output.txt","w") as o:
        for line in i:
            o.write(line)

# shutil.copy(fajlbol,fajlba)

read_io()
write_io()
open_with_with()
copy_2()