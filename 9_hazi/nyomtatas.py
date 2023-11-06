def main():
    pages = "4-7,8,9,15"
    li = []
    for c in pages.split(','):
        if c.isdigit():
            li.append(int(c))
        else:
            [li.append(i) for i in range(int(c[0]),int(c[-1])+1)] 
    print(li)

if __name__ == "__main__":
    main()