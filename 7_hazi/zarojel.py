def ellenorzo(s):
    beginning = []
    
    for c in s:
        if c in "({[":
            beginning.append(c)
        elif c == ')' and beginning[-1] == '(':
            beginning.pop()
        elif c == ']' and beginning[-1] == '[':
            beginning.pop()
        elif c == '}' and beginning[-1] == '{':
            beginning.pop()
    if beginning:
        return False
    return True

def ellenorzo2(s):
    beginning = []
    cases = dict(zip("{[(","}])"))
    for c in s:
        if c in "([{":
            beginning.append(c)
        elif c in "])}":
            if cases[beginning[-1]] == c:
                beginning.pop()
    return bool(not beginning)

            


def main():
    s1 = "((5+3)*2+1)"
    s2 = "{[(3+1)+2]+}"
    s3 = "(3+{1-1)}"
    s4 = "[1+1]+(2*2)-{3/3}"
    s5 = "(({[(((1)-2)+3)-3]/3}-3)"
    [print(ellenorzo(s)) for s in [s1,s2,s3,s4,s5]]
    [print(ellenorzo2(s)) for s in [s1,s2,s3,s4,s5]]
    


if __name__ == "__main__":
    main()