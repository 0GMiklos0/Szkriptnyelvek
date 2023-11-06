def main():
    summ = 0

    for i in range(1000000):
        normal_digits = [int(n) for n in str(i)]
        bin_digits = [n for n in str(bin(i))[2:]]
        if bin_digits == bin_digits[::-1] and normal_digits == normal_digits[::-1]:
            summ += i
    print(summ) 

if __name__ == "__main__":
    main()