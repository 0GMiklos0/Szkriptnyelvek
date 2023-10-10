def main():
    num = [1122, 1111]
    br = [int(i) for i in str(num[0])]
    br2 = [int(i) for i in str(num[1])]
    sum = 0
    for i in range(len(br)-1):
        if br[i] == br[i+1]:
            sum += br[i]
    for i in range(len(br2)-1):
        if br[i] == br[i+1]:
            sum += br[i]


if __name__ == "__main__":
    main()