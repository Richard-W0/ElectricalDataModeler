######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Richard Wong
# Opiskelijanumero: 002584058
# Päivämäärä: 30.10.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Kaverini Erik (ei LUT opsiskelija) auttoi strukturaalisoimisessa, idea nestatuista hashmapeistä on hänen, Säde Karanta auttoi debuggaamisessa ja käytin chatgpt:tä debuggaamiseen myös mutta riviäkään koodia ei ole siltä kopioitu
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
    lib.TIEDOSTO.lista = []
    lib.TIEDOSTO.viikottainen = {}
    lib.TIEDOSTO.kuukausittainen = {}
    
    while True:
        valinta = valikko()
        if valinta == 1:
            nimiLuettava = lib.kysyNimi(1)
            lib.lueTiedosto(nimiLuettava)
        elif valinta == 2:
            if len(lib.TIEDOSTO.lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                lib.analysoiTiedostoKuukaudet()
        elif valinta == 3:
            if len(lib.TIEDOSTO.lista) == 0:
                print("Ei tietoja tallennettavaksi, analysoi tiedot ennen tallennusta.")
            else:   
                nimiKirjoitettava = lib.kysyNimi(2)
                lib.kirjoitaTiedostoonKuukausittainen(nimiKirjoitettava)
        elif valinta == 4:
            if len(lib.TIEDOSTO.lista) == 0:
                print("Ei tietoja analysoitavaksi, lue tiedot ennen analyysiä.")
            else:
                lib.analysoiTiedostoPaivat()
                nimiKirjoitettava = lib.kysyNimi(2)
                lib.kirjoitaTiedostoonViikottainen(nimiKirjoitettava)
        elif valinta == 0:
            print("Lopetetaan.")
            break
        else:
            print("Tuntematon valinta, yritä uudestaan.")
        print()
    lib.TIEDOSTO.lista.clear()
    lib.TIEDOSTO.viikottainen.clear()
    lib.TIEDOSTO.kuukausittainen.clear()
    
    return None

paaohjelma()
print()
print("Kiitos ohjelman käytöstä.")
# eof
