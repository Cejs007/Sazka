from funkce import vsad_sportku, losuj_sportku


def dokud_nevyhraju(stastna_cisla):
    stastna_cisla.sort()
    los = losuj_sportku()
    los.sort()
    iterace = 1
    while stastna_cisla != los:
        los = losuj_sportku()
        los.sort()
        iterace += 1
        if iterace % 1000000 == 0:
            print(iterace, los)
    return iterace


if __name__ == '__main__':
    stastna_cisla = vsad_sportku()
    iterace = dokud_nevyhraju(stastna_cisla)
    print(f"Čekal bych {iterace / 3 / 52 / 10} let a prosázel {iterace * 20} Kč.")
