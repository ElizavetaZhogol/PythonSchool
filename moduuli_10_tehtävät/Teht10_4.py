# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle.
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista.
# Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi.
# Luokassa on seuraavat metodit:

# tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet
# eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.

# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän.
# Muussa tapauksessa palautetaan False.
# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli".
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä.
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia,
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random
import pandas

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenMuutos):

        muutos = self.nopeus + nopeudenMuutos

        if 0 <= muutos <= self.huippunopeus:

           self.nopeus = muutos 
        
        elif muutos < 0:

            self.nopeus = 0

        elif muutos > self.huippunopeus:

            self.nopeus = self.huippunopeus
        
    
    def kulje(self, tunti):

        matkaMuutos = self.nopeus * tunti

        self.matka = self.matka + matkaMuutos

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot
        self.tunti = 0
        
    def tunti_kuluu(self):

        self.tunti = self.tunti + 1

        for auto in self.autot:

            nopeudenMuutos = random.randint(-10, 15)
        
            auto.kiihdyta(nopeudenMuutos)

            auto.kulje(1) 

        tuntikulu = self.tunti % 10

        if tuntikulu == 0:

            print(f"\n{self.tunti} tuntia on kulunut\n")

            print(self.tulosta_tilanne())

    def tulosta_tilanne(self):

        tiedot = []

        for auto in self.autot:

            tieto = auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka

            tiedot.append(tieto)

        tauluko = pandas.DataFrame(tiedot, columns=["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"])

        return tauluko
    
    def kilpailu_ohi(self):

        for auto in self.autot:

            if auto.matka >= self.pituus:

                return True

        return False

autot = []

for i in range(10):

    rekisteritunnus = "ABC-" + str(i + 1)

    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)

    autot.append(auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

print(kilpailu)

kilpailu_tulos = kilpailu.kilpailu_ohi()

while not kilpailu.kilpailu_ohi():

    kilpailu.tunti_kuluu()

print("\nKilpailu on ohi!\n")

print(kilpailu.tulosta_tilanne())