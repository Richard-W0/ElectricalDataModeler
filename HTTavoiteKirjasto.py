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
    try:
        tiedosto = open(tiedostoNimi, "r")
        rivi = tiedosto.readline() #skipataan eka rivi
        while len(rivi) > 0:
            pass
    except FileNotFoundError:
        


def analysoiTiedosto():
    #analysoi tiedoston

def kirjoitaTiedostoon():
    #kirjoittaa tiedostoon


# eof
