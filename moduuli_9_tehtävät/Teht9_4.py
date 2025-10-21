# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
# Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
# Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
# Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

# Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
# Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.

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
    
autot = []

for i in range(10):

    rekisteritunnus = "ABC-" + str(i + 1)

    huippunopeus = random.randint(100, 200)

    auto = Auto(rekisteritunnus, huippunopeus)

    autot.append(auto)

kokonaismatka = 0

while kokonaismatka < 10000:

    for auto in autot:

        nopeudenMuutos = random.randint(-10, 15)
        
        auto.kiihdyta(nopeudenMuutos)

        auto.kulje(1)

        if kokonaismatka < auto.matka:

            kokonaismatka = auto.matka 

tiedot = []

for auto in autot:

    tieto = auto.rekisteritunnus, auto.huippunopeus, auto.nopeus, auto.matka

    tiedot.append(tieto)

tauluko = pandas.DataFrame(tiedot, columns=["Rekisteritunnus", "Huippunopeus", "Nopeus", "Matka"])

print("\nAutokilpailun tulokset \n")

print(tauluko)