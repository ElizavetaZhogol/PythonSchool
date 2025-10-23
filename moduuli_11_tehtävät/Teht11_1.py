# Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti.
# Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja.
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot.
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua).
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumärä):
        self.kirjoittaja = kirjoittaja
        self.sivumärä = sivumärä
        super().__init__(nimi)

    def tulosta_tiedot(self):

        print(f"\nJulkaisun nimi: {self.nimi}")
        print(f"\nKirjoittaja: {self.kirjoittaja}")
        print(f"\nSivumärä: {self.sivumärä}")

class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):

        print(f"\nJulkaisun nimi: {self.nimi}")
        print(f"\nPäätoimittaja: {self.päätoimittaja}")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulosta_tiedot()

lehti.tulosta_tiedot()