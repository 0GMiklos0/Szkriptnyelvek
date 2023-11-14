ALPHABET = ''.join([chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)])

def normalize(s):
    return s.replace(' ','').lower()

def is_anagramma(s1, s2):
    if sorted(list(normalize(s1))) == sorted(list(normalize(s2))):
        return f"{s1} es {s2} anagrammak"

def is_anagramma2(s1, s2):
    szotar1 = {}
    szotar2 = {}
    for ch in normalize(s1):
        szotar1[ch] = szotar1.get(ch,0) + 1
    for ch in normalize(s2):
        szotar2[ch] = szotar2.get(ch,0) + 1
    if szotar1 == szotar2:
        print(f"{s1} es {s2} anagrammak")

def main():
    str1 = 'Clint Eastwood'
    str2 = 'Old west action'
    #print(ALPHABET)
    is_anagramma(str1,str2)
    is_anagramma2(str1,str2)
    
if __name__ == "__main__":
    main()