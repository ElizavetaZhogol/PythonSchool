# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina.
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina.
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa.
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l).
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.

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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        self.akkukapasiteetti = akkukapasiteetti
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):

        print(f"\nSähköauton rekisteritunnus: {self.rekisteritunnus}.")
        print(f"\nSähköauton huippunopeus: {self.huippunopeus} km/h.")
        print(f"\nSähköauton akkukapasiteetti: {self.akkukapasiteetti} KWh.")
        print(f"\nSähköauton nopeus: {self.nopeus} km/h.")
        print(f"\nSähköauton matka: {self.matka} km.")
        


class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankin_koko):
        self.bensatankin_koko = bensatankin_koko
        super().__init__(rekisteritunnus, huippunopeus)

    def tulosta_tiedot(self):

        print(f"\nPolttomoottoriauton rekisteritunnus: {self.rekisteritunnus}.")
        print(f"\nPolttomoottoriauton huippunopeus: {self.huippunopeus} km/h.")
        print(f"\nPolttomoottoriauton bensatankin koko: {self.bensatankin_koko} l.")
        print(f"\nPolttomoottoriauton nopeus: {self.nopeus} km/h.")
        print(f"\nPolttomoottoriauton matka: {self.matka} km.")

sähköauto = Sähköauto("ABC-15", 180, 52.5)

polttomoottoriauto = Polttomoottoriauto("ACD-123", 165, 32.3)

sähköauto.kiihdyta(146)

polttomoottoriauto.kiihdyta(125)

sähköauto.kulje(3)

polttomoottoriauto.kulje(3)

print("\nTulokset sähköautolle:")

sähköauto.tulosta_tiedot()

print("\nTulokset polttomoottoriautolle:")

polttomoottoriauto.tulosta_tiedot()

