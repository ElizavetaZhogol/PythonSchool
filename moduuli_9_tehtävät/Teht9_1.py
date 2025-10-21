# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.hetkinenNopeus = 0
        self.kuljettuMatka = 0

auto = Auto("ABC-123", "142 km/h")

print(f"\nAuton rekisteritunnus on {auto.rekisteritunnus:s}." )
print(f"\nAuton huippunopeus on {auto.huippunopeus:s}.")
print(f"\nAuton tämänhetkinen nopeus on {auto.hetkinenNopeus:d} km/h.")
print(f"\nAuton kuljettu matka on {auto.kuljettuMatka:d} km.\n")