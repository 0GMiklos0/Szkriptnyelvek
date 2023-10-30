def main():
    with open("8_hazi/bemenet.txt", "r") as f:
        crate = f.read().splitlines()
        crate = [l.replace('\t', ' ').split(' ') for l in crate]
        summ = 0
        for l in crate:
            nums = [int(i) for i in l]
            summ += max(nums)-min(nums)
        print(summ)

        

if __name__ == "__main__":
    main()
