TEXT = """

"A katalán zászló, a Senyera színeit fogja viselni a következő idény során a spanyol élvonalban szereplő FC Barcelona labdarúgócsapata.

A Marca című sportnapilap hétfői internetes kiadása szerint az együttes játékosai az idegenbeli mérkőzéseken húzzák majd magukra a sárga-piros csíkozású mezt - első ízben a klub történelme során.

A döntés várhatóan nem marad politikai visszhang nélkül Spanyolországban, tekintettel a katalán önállósodási törekvésekre." """.strip()

def main():
    n_text = TEXT
    umlaut = "áéíóöőúüűÁÉÍÓÖŐÚÜŰ"
    non_umlaut = "aeiooouuuAEIOOOUUU"
    changer = {}
    for i in range(len(umlaut)):
        changer[umlaut[i]] = non_umlaut[i]
    for k in changer.keys():
        n_text = n_text.replace(k,changer[k])
    print(n_text)
if __name__ == "__main__":
    main()