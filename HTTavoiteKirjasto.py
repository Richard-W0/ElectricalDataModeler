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
    Tiedosto.lista.clear()
    try:
        tiedosto = open(tiedostoNimi, "r")
        rivi = tiedosto.readline() #skipataan eka rivi
        rivi = tiedosto.readline()
        while len(rivi) > 0:
            strip = rivi.strip()
            riviS = strip.split(";")
            aika = time.strptime(riviS[0], "%d-%m-%Y %H:%M")
            kwhNight = float(riviS[1])
            kwhDay = float(riviS[2])
            Tiedosto.lista.append((aika, kwhNight, kwhDay))
            rivi = tiedosto.readline()
        tiedosto.close()
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt, yritä uudestaan.")
        


def analysoiTiedostoKuukaudet():
    Tiedosto.kuukausittainen.clear()

    for arvo in Tiedosto.lista:

        aika = arvo[0]
        kwhNight = arvo[1]
        kwhDay = arvo[2]

        kuukausiNimi = time.strftime("%b", aika)

        if kuukausiNimi not in Tiedosto.kuukausittainen:
            Tiedosto.kuukausittainen[kuukausiNimi] = {"Yö" : 0, "Päivä" : 0, "Yhteensä" : 0}

        Tiedosto.kuukausittainen[kuukausiNimi]["Yö"] += kwhNight / 1000 #muunnetaan kwh mwh:hon
        Tiedosto.kuukausittainen[kuukausiNimi]["Päivä"] += kwhDay / 1000
        Tiedosto.kuukausittainen[kuukausiNimi]["Yhteensä"] += (kwhDay + kwhNight) / 1000

def analysoiTiedostoPaivat():
    Tiedosto.viikottainen.clear()

    viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]


def kirjoitaTiedostoon():
    #kirjoittaa tiedostoon


#eof
