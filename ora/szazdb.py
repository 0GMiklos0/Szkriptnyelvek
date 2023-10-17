INPUT = "szazdb_input.txt"

def main():
    with open(INPUT,"r") as f:
        summ = 0
        szamok = f.read().splitlines()
        for i in szamok:
            summ += int(i)
        print(str(summ)[0:10])
            
if __name__ == "__main__":
    main()