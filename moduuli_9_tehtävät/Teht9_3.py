# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, nopeudenMuutos):

        muutos = self.nopeus + nopeudenMuutos

        if 0 < muutos <= self.huippunopeus:

           self.nopeus = muutos 
        
        elif muutos < 0:

            self.nopeus = 0

        elif muutos > self.huippunopeus:

            self.nopeus = self.huippunopeus
        
        return self.nopeus
    
    def kulje(self, tunti):

        matkaMuutos = self.nopeus * tunti

        self.matka = self.matka + matkaMuutos

        return self.matka
    
auto = Auto("ABC-123", 142)

auto.matka = 2000

print(f"\nAuto ajoi matkan: {auto.matka} km")

print(f"\n+60 km/h: {auto.kiihdyta(60)} km/h")

print(f"\n60 km/h * 1.5h. Uusi kuljettu matka on: {auto.kulje(1.5):.0f} km\n")




