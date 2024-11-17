######################################################################
# CT60A0203 Ohjelmoinnin perusteet
# Tekijä: Richard Wong
# Opiskelijanumero: 
# Päivämäärä: 30.10.2024
# Kurssin oppimateriaalien lisäksi työhön ovat vaikuttaneet seuraavat
# lähteet ja henkilöt, ja se näkyy tehtävässä seuraavalla tavalla:
# Kaverini Erik (ei LUT opsiskelija) auttoi strukturaalisoimisessa, idea nestatuista hashmapeistä on hänen, ja hän myös näytti matriisin summaukseen liittyviä asioita (axis = 1 ja axis = 0 komennot)Säde Karanta auttoi debuggaamisessa ja käytin chatgpt:tä debuggaamiseen myös mutta riviäkään koodia ei ole siltä kopioitu
# Mahdollisen vilppiselvityksen varalta vakuutan, että olen tehnyt itse
# tämän tehtävän ja vain yllä mainitut henkilöt sekä lähteet ovat
# vaikuttaneet siihen yllä mainituilla tavoilla.
######################################################################
# Tehtävä Harjoitustyö
import time
import os
import sys
import numpy as np
from datetime import datetime

viikonpaivat = ["Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai", "Sunnuntai"]

class TIEDOSTO:
    lista = []
    viikottainen = {}
    kuukausittainen = {}
    lampotila = {}
    viikkoMatriisi = np.zeros((54, 3), dtype=float) #dateitime laskee viikkojen sijaan maanantait joten 54

def kysyNimi(n):
    if n == 1:
        return input("Anna luettavan tiedoston nimi: ") 
    elif n == 2:
        return input("Anna kirjoitettavan tiedoston nimi: ")
    return None

def lueTiedosto(tiedostoNimi):
    TIEDOSTO.lista.clear()
    try:
        tiedosto = open(tiedostoNimi, "r", encoding="UTF-8")
        rivimaara = 0
        rivi = tiedosto.readline() #skipataan eka rivi
        rivi = tiedosto.readline()
        while len(rivi) > 0:
            strip = rivi.strip()
            riviS = strip.split(";")
            aika = time.strptime(riviS[0], "%d-%m-%Y %H:%M")
            kwhNight = float(riviS[1])
            kwhDay = int(float(riviS[2])
            TIEDOSTO.lista.append((aika, kwhNight, kwhDay))
            rivimaara += 1
            rivi = tiedosto.readline()
        tiedosto.close()
        print("Tiedostosta '{0:s}' lisättiin listaan {1} datariviä.".format((tiedostoNimi), (rivimaara)))
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None

def analysoiTiedostoKuukaudet():
    TIEDOSTO.kuukausittainen.clear()
    kuukaudet = 0

    for arvo in TIEDOSTO.lista:

        aika= arvo[0]
        kwhNight = arvo[1]
        kwhDay = arvo[2]

        kuukausiNimi = time.strftime("%b", aika)

        if kuukausiNimi not in TIEDOSTO.kuukausittainen:
            TIEDOSTO.kuukausittainen[kuukausiNimi] = {"Yö" : 0, "Päivä" : 0, "Yhteensä" : 0}

        TIEDOSTO.kuukausittainen[kuukausiNimi]["Yö"] += kwhNight / 1000 #muunnetaan kwh mwh:hon
        TIEDOSTO.kuukausittainen[kuukausiNimi]["Päivä"] += kwhDay / 1000
        TIEDOSTO.kuukausittainen[kuukausiNimi]["Yhteensä"] += (kwhDay + kwhNight) / 1000
    for key in TIEDOSTO.kuukausittainen.items():
        kuukaudet +=1
    print("Kuukausittaiset summat laskettu", kuukaudet, "kuukaudelle.")
    return None

def analysoiTiedostoPaivat():
    TIEDOSTO.viikottainen.clear()

    for paiva in viikonpaivat:
        TIEDOSTO.viikottainen[paiva] = 0 #initialisoidaan hashmappi

    for aika, kwhNight, kwhDay in TIEDOSTO.lista:
        viikonpaivaIndeksi = int(time.strftime("%w", aika))
        viikonpaivaIndeksi = (viikonpaivaIndeksi + 6) % 7 #if this works Im the smartest man alive
        viikonpaivaSuomeksi = viikonpaivat[viikonpaivaIndeksi]

        totalMwh = (kwhDay + kwhNight) / 1000
        TIEDOSTO.viikottainen[viikonpaivaSuomeksi] += totalMwh
    return None

def kirjoitaTiedostoonKuukausittainen(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Kuukausittaiset kulutukset (MWh):\n")
        tiedosto.write("Kuukausi;Yö;Päivä;Yhteensä\n")
        for kuukausi, arvot in TIEDOSTO.kuukausittainen.items():
            tiedosto.write("{0};{1:.1f};{2:.1f};{3:.1f}\n".format(kuukausi, arvot["Yö"], arvot["Päivä"], arvot["Yhteensä"]))
        tiedosto.close()
        print("Tiedosto '{0:s}' kirjoitettu.".format(tiedostoNimi))

    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None

def kirjoitaTiedostoonViikottainen(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Viikonpäivä;Kulutus (MWh)\n")
        for paiva, kulutus in TIEDOSTO.viikottainen.items():
            tiedosto.write("{0};{1:.1f}\n".format(paiva, kulutus))
        tiedosto.close()
        print("Tiedosto '{0:s}' kirjoitettu.".format(tiedostoNimi))
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None

def lueLampotila(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "r", encoding="UTF-8")
        rivi = tiedosto.readline() #skipataan eka rivi
        rivi = tiedosto.readline()
        while len(rivi) > 0:
            strip = rivi.strip()
            riviS = strip.split(",")
            paivaL = time.strptime(riviS[0], "%Y.%m.%d")
            lampotila = float(riviS[1])
            TIEDOSTO.lampotila[time.strftime("%d.%m.%Y", paivaL)] = lampotila
            rivi = tiedosto.readline()

        tiedosto.close()
        print("Tiedosto '{0}' luettu.".format(tiedostoNimi))
        print("Tiedot yhdistetty.")
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None

def kirjoitaLampotila(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Päivittäiset kulutukset (kWh) ja lämpötila:\n")
        tiedosto.write("Pvm;Yö;Päivä;Yhteensä;Lämpötila\n")

        paivittainenKulutus = {}

        for aika, kwhNight, kwhDay in TIEDOSTO.lista:
            paiva = time.strftime("%d.%m.%Y", aika)
            if paiva not in paivittainenKulutus:
                paivittainenKulutus[paiva] = {"Päivä": 0, "Yö": 0} #Lisää nestattuja hashmappeja
            paivittainenKulutus[paiva]["Päivä"] = np.add(paivittainenKulutus[paiva]["Päivä"], float(kwhDay))
            paivittainenKulutus[paiva]["Yö"] = np.add(paivittainenKulutus[paiva]["Yö"], float(kwhNight))

        for key, value in paivittainenKulutus.items():
            lampotila = TIEDOSTO.lampotila.get(key)
            yhteensa = np.add(value["Yö"], value["Päivä"])
            tiedosto.write("{0};{1:.1f};{2:.1f};{3:.1f};{4}\n".format(key, value["Yö"], value["Päivä"], yhteensa, lampotila))

        tiedosto.close()
        print("Tiedosto '{0:s}' kirjoitettu.".format(tiedostoNimi))
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None

def analysoiMatriisi():
    for aika, kwhNight, kwhDay in TIEDOSTO.lista:
        viikko = int(time.strftime("%W", aika))
        tunti = aika.tm_hour
        kulutus = (kwhDay + kwhNight) / 1000
        if tunti < 8:
            sarake = 0
        elif tunti < 16:
            sarake = 1
        else:
            sarake= 2
        TIEDOSTO.viikkoMatriisi[viikko][sarake] += kulutus
    print("Matriisianalyysi suoritettu.")
    return None

def kirjoitaMatriisi(tiedostoNimi):
    try:
        tiedosto = open(tiedostoNimi, "w")
        tiedosto.write("Viikko;Klo 0-8;Klo 8-16;Klo 16-24;Viikkosumma\n")
        summat = np.sum(TIEDOSTO.viikkoMatriisi, axis = 1)
        summatSarake = np.sum(TIEDOSTO.viikkoMatriisi, axis = 0)
        summanSumma = 0
        for i in range(len(summat)):
            tiedosto.write("Vko {0};{1:.1f};{2:.1f};{3:.1f};{4:.1f}\n".format(i, TIEDOSTO.viikkoMatriisi[i][0], TIEDOSTO.viikkoMatriisi[i][1], TIEDOSTO.viikkoMatriisi[i][2], summat[i])) 
        for summa in summat:
            summanSumma += summa
        tiedosto.write("Yhteensä;{0:.1f};{1:.1f};{2:.1f};{3:.1f}".format(summatSarake[0], summatSarake[1], summatSarake[2], summanSumma))

        tiedosto.close()
        print("Tiedosto '{0:s}' kirjoitettu.".format(tiedostoNimi))
    except OSError:
        print("Tiedoston '{0:s}' käsittelyssä virhe, lopetetaan.".format(tiedostoNimi))
        sys.exit(0)
    return None
#eof
