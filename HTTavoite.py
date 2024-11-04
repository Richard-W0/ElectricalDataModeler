######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Richard Wong
# Opiskelijanumero: 
# Päivämäärä: 30.10.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
#
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä Harjoitustyö

def valikko():
    valikko = """Valitse haluamasi toiminto:
1) Lue tiedosto
2) Analysoi
3) Kirjoita tiedosto
4) Analysoi viikonpäivittäiset tulokset
0) Lopeta"""
    print(valikko)
    return int(input("Anna valintasi: "))


def paaohjelma():
    
    while True:
        valinta = valikko()
        if valinta == 1:
            pass
        elif valinta == 2:
            pass
        elif valinta == 3:
            pass
        elif valinta == 4:
            pass
        elif valinta == 0:
            print("Lopetetaan.")
            break

paaohjelma()

# eof
