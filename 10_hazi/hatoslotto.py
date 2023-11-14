def is_prime(n):
    """
    Decide whether a number is prime or not.
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    maxi = n**0.5 + 1
    while i <= maxi:
        if n % i == 0:
            return False
        i += 2

    return True

def main():
    summ = 90
    mult = 996300
    li = []
    actual_numbers = []
    buffered_number = 0
    primenums = [i for i in range(91) if is_prime(i)]
    for i in primenums[::-1]:
        while mult % i == 0:
            li.append(i)
            mult /= i
    print(li)
    while summ != 0:
        
        



if __name__ == "__main__":
    main()