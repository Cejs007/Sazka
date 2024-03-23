from random import sample


def vsad_sportku(start=1, end=49, n=6):
    '''
    Funkce vezme od uživatele 6 čísel a zkontroluje, zda jsou ve správném formátu
    a rozsahu. Vrací 6 unikátních hodnot.
    '''
    # zadefinovat místo kam budu ukládat vybraná čísla
    moje_stastna_cisla = []
    # iterace dokud nemám 6 čísel
    while True:
        # input - zadání čísla
        cislo = input(f"Zakřížkuj číslo od {start} do {end}: ")
        # ošetření nečíselného vstupu
        try:
            cislo = int(cislo)
        except ValueError:
            print(f"{cislo} není číslo.")
            continue
        # kontrola 1 -> je číslo z rozsahu 1 - 49?
        if not start <= cislo <= end:
            print(f"{cislo} mimo rozsah.")
            continue
        # kontrola 2 -> je to nové číslo (nesmí se opakovat)
        if cislo in moje_stastna_cisla:
            print(f"{cislo} už mám.")
            continue
        # pokud ok -> přidat číslo, pokud ne pokračovat v iteraci
        moje_stastna_cisla.append(cislo)
        # zastavení smyčky po dosažení 6 čísel
        if len(moje_stastna_cisla) == n:
            break
    return moje_stastna_cisla


def losuj_sportku(start=1, end=49, n=6):
    '''
    Returns n random unique numbers from start to end.
    '''
    return sample(range(start, end + 1), n)


def dokud_nevyhraju(vsazena_cisla):
    pocet_losovani = 0
    vsazena_cisla.sort()
    while True:
        los = losuj_sportku()
        los.sort()
        pocet_losovani += 1
        if pocet_losovani % 1000000 == 0:
            print(pocet_losovani, vsazena_cisla, los)
        if los == vsazena_cisla:
            break
    return pocet_losovani
