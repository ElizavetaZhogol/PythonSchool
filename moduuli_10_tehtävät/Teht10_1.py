# Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
# Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5),
# metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa,
# että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat,
# missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten,
# että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.

class Hissi:
    def __init__(self, alkerros, ylkerros):
        self.alkerros = alkerros
        self.ylkerros = ylkerros
        self.kerros = alkerros

    def siirry_kerrokseen(self, siiry_kerros):

        if siiry_kerros >= self.alkerros and siiry_kerros <= self.ylkerros:

            while self.kerros != siiry_kerros:

                if self.kerros > siiry_kerros:

                    self.kerros = self.kerros_alas()

                elif self.kerros < siiry_kerros:

                    self.kerros = self.kerros_ylös()

                print(f"Olet nyt {self.kerros} kerroksessa.")

        else:

            print(f"Et voi mennä kerrokseen {siiry_kerros}.")


    def kerros_ylös(self):

        self.kerros = self.kerros + 1

        return self.kerros

        
    def kerros_alas(self):

        self.kerros = self.kerros - 1

        return self.kerros
    
hissi = Hissi(1, 10)

print(f"Aloitat liikkumisen aivan alimmasta {hissi.alkerros} kerroksesta.")

hissi.siirry_kerrokseen(5)

print(f"Olet saapunut {hissi.kerros} kerrokseen.")

hissi.siirry_kerrokseen(hissi.alkerros)

print(f"Olet laskeutunut {hissi.alkerros} ja alimpaan kerrokseen.")