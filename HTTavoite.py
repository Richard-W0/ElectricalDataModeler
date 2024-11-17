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
import HTTavoiteKirjasto as lib
import sys

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
            nimiLuettava = lib.kysyNimi(1)
            lib.lueTiedosto(nimiLuettava)
        elif valinta == 2:
            lib.analysoiTiedostoKuukaudet()
        elif valinta == 3:
            nimiKirjoitettava = lib.kysyNimi(2)
            lib.kirjoitaTiedostoonKuukausittainen(nimiKirjoitettava)
        elif valinta == 4:
            lib.analysoiTiedostoPaivat()
            nimiKirjoitettava = lib.kysyNimi(2)
            lib.kirjoitaTiedostoonViikottainen(nimiKirjoitettava)
        elif valinta == 0:
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestan.")
    return None

paaohjelma()

# eof
