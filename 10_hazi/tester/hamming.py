def hammingDistance(a: str, b):
    if len(a) != len(b):
        return -1
    li = [a[i] for i in range(len(a)) if b[i] != a[i]]
    return len(li)

print(hammingDistance('acaa','abba'))