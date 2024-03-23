from random import randint


def vsad_sportku(pocet_cisel=6, od=1, do=49):
    '''
    Funkce vsaď Sportku, kdy si uživatel
    vybere 6 čísel od 1 do 49 bez opakování
    '''

    cisla = []
    while len(cisla) < pocet_cisel:
        try:
            cislo = int(input("Zadej své šťastné číslo: "))
        except ValueError:
            print("Nezadal jsi celé číslo!")
            continue
        if cislo in cisla:
            print("Zadal jsi číslo, které už mám!")
            continue
        if do >= cislo >= od:
            print(f"Zadal jsi {cislo}")
            cisla.append(cislo)
        else:
            print(f"Zadané číslo mimo rozsah {od} - {do}!")
    return cisla


def losuj_sportku(pocet_cisel=6, od=1, do=49):
    '''
    Funkce losování Sportky náhodně vyberte 6 čísel
    bez opakování z čísel od 1 do 49
    '''
    cisla = []
    while len(cisla) < pocet_cisel:
        cislo = randint(od, do)
        if cislo not in cisla:
            cisla.append(cislo)
    return cisla


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    vsazeno = vsad_sportku()
    print(f"Šťastná čísla: {sorted(vsazeno)}")
    losovano = losuj_sportku()
    print(f"Vylosovaná čísla: {sorted(losovano)}")
