from funkce import vsad_sportku, dokud_nevyhraju

vsazena_cisla = vsad_sportku()

pocet_losovani_vyhra = dokud_nevyhraju(vsazena_cisla)

LOSOVANI_TYDEN = 3
TYDNY_ROK = 52
SLOUPCE_LOSOVANI = 10
SLOUPEC_KC = 20

print(pocet_losovani_vyhra / LOSOVANI_TYDEN / SLOUPCE_LOSOVANI / TYDNY_ROK, pocet_losovani_vyhra * SLOUPEC_KC)
