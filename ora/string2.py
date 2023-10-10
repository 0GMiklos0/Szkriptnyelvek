#!/usr/bin/env python3
# coding: utf-8

# További sztring műveletek


# E. verbing
# Ha az adott sztring hossza legalább 3, akkor
# a végéhez adjuk hozzá az 'ing' ragot.
# Ha 'ing'-re végződik, akkor ehelyett az 'ly'
# ragot tegyük hozzá.
# Ha a sztring hossza rövidebb 3 karakternél, akkor
# hagyjuk változatlanul.
# Adjuk vissza az eredménysztringet.
def verbing(s):
    if len(s) < 3:
        return s
    elif s[-3:] == "ing":
        return s + "ly"
    else:
        return s + "ing"

# F. not_bad
# Egy adott sztringben keressük meg a 'not' és
# 'bad' szavak előfordulási helyét. Ha a 'bad'
# a 'not' szót követi, akkor cseréljük ki az
# egész 'not'...'bad' részsztringet a 'good' szóra.
# Adjuk vissza az eredmény sztringet.
# Példa: 'This dinner is not that bad!' ->
#        This dinner is good!
def not_bad(s):
    if s.find("not") < s.find("bad"):
        new_s = s[:s.find("not")] + "good" + s[s.find("bad")+3:]
        return new_s
    else:
        return s
# G. front_back
# Egy sztringet osszunk két részre, s a két részt nevezzük
# a sztring elejének és végének. Ha a sztring hossza páros, akkor
# a két rész hossza azonos. Ha a hossz páratlan, akkor az eleje
# legyen egy karakterrel hosszabb mint a vége.
# Például 'abcde' esetén a két rész: 'abc' és 'de'.
# Két adott sztring (a és b) esetén adjunk vissza egy sztringet, mely
# a következőképpen épül fel:
# a-eleje + b-eleje + a-vége + b-vége
# Például ha a = 'abcd' és b = 'xy', akkor az eredmény 'abxcdy' legyen.
def front_back(a, b):
    if len(a) % 2 == 0:
        a_part_1 = a[:len(a)//2]
        a_part_2 = a[len(a)//2:]
    else:
        a_part_1 = a[:len(a)//2+1]
        a_part_2 = a[len(a)//2+1:]
    if len(b) % 2 == 0:
        b_part_1 = b[:len(b)//2]
        b_part_2 = b[len(b)//2:]
    else:
        b_part_1 = b[:len(b)//2+1]
        b_part_2 = b[len(b)//2+1:]
    combine = a_part_1 + b_part_1 + a_part_2 + b_part_2
    return combine

# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

#if __name__ == '__main__':
main()
