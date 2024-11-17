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
import os
import sys
#import numpy as np


viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

class Tiedosto:
    lista = []
    viikottainen = {}
    kuukausittainen = {}

def kysyNimi(n):
    if n == 1:
        return input("Anna luettavan tiedoston nimi: ") 
    elif n == 2:
        return input("Anna kirjoitettavan tiedoston nimi: ")
    return None


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
    except OSError:
        print("Tiedostoa ei löytynyt, yritä uudestaan.")
    return None
        


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
    return None

def analysoiTiedostoPaivat():
    Tiedosto.viikottainen.clear()

    for paiva in viikonpaivat:
        Tiedosto.viikottainen[paiva] = 0 #initialisoidaan hashmappi

    for aika, kwhNight, kwhDay in Tiedosto.lista:
        viikonpaivaIndeksi = int(time.strftime("%w", aika))
        viikonpaivaSuomeksi = viikonpaivat[viikonpaivaIndeksi]

        totalMwh = (kwhDay + kwhNight) / 1000
        Tiedosto.viikottainen[viikonpaivaSuomeksi] += totalMwh
    return None


def kirjoitaTiedostoonKuukausittainen(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Kuukausittaiset kulutukset (MWh):\n")
        tiedosto.write("Kuukausi;Yö;Päivä;Yhteensä\n")
        for kuukausi, arvot in Tiedosto.kuukausittainen.items():
            tiedosto.write("{0};{1:.1f};{2:.1f};{3:.1f}\n".format(
                kuukausi, arvot["Yö"], arvot["Päivä"], arvot["Yhteensä"]))
        tiedosto.close()
    except OSError:
        print("Virhe tiedostoon kirjoittamisessa:")
        sys.exit(0)
    return None

def kirjoitaTiedostoonViikottainen(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Viikonpäivä;Kulutus (MWh)\n")
        for paiva, kulutus in Tiedosto.viikottainen.items():
            tiedosto.write("{0};{1:.1f}\n".format(paiva, kulutus))
        tiedosto.close()
    except OSError:
        print("Virhe tiedostoon kirjoittamisessa:")
        sys.exit(0)
    return None

#Lue tiedostoon OS error
#if len data == 0 ei tietoaja analysoitavaksi
#kirjoita tiedostoon OS error kanssa (sys.exit(0))
#viikkoanalyysiin sama os error try exceptiin

#eof
