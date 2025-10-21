# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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
        
        return self.nopeus


auto = Auto("ABC-123", 142)

print(f"+30 km/h: {auto.kiihdyta(30)} km/h")

print(f"+70 km/h: {auto.kiihdyta(70)} km/h")

print(f"+50 km/h: {auto.kiihdyta(50)} km/h")

print(f"-200 km/h: {auto.kiihdyta(-200)} km/h")

        
