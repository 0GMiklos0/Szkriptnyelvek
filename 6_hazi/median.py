def test(li):
    li.sort()
    var = int(len(li)/2)
    if len(li) % 2 == 0:
        median = (li[var-1] + li[var]) / 2
    else:
        median = li[var]
    return median

def main():
    print(test([1, 2, 3, 4, 5]) == 3)
    print(test([3, 1, 2, 5, 3]) == 3)
    print(test([1, 300, 2, 200, 1]) == 2)
    print(test([3, 6, 20, 99, 10, 15]) == 12.5)

if __name__ == "__main__":
    main()