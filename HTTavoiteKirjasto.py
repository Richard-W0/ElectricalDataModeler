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
import time
import math
import numpy as np

class Tiedosto:
    lista = []
    viikottainen = {}
    kuukausittainen = {}

def kysyNimi(n):
    if n == 1:
        return input("Anna luettavan tiedoston nimi: ") 
    elif n == 2:
        return input("Anna kirjoitettavan tiedoston nimi: ")


def lueTiedosto(tiedostoNimi):
    tiedostoLista = []
    try:
        tiedosto = open(tiedostoNimi, "r")
        rivi = tiedosto.readline() #skipataan eka rivi
        while len(rivi) > 0:
            strip = rivi.strip()
            riviS = strip.split(";")
            aika = time.strptime(riviS[0], "%d-%m-%Y %H:%M")
            kwhNight = float(riviS[1])
            kwhDay = float(riviS[2])
            tiedostoLista.append((aika, kwhNight, kwhDay))
        tiedosto.close()
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt, yritä uudestaan.")
        


def analysoiTiedostoKuukaudet():
    #analysoi tiedoston

def analysoiTiedostoPäivät():
    pass

def kirjoitaTiedostoon():
    #kirjoittaa tiedostoon


# eof
