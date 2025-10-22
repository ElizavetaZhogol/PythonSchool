# Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan.
# Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä.
# Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

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
    
class Talo:
    def __init__(self, alkerros, ylkerros, hissi_maara):
        self.alkerros = alkerros
        self.ylkerros = ylkerros
        self.hissit = []

        for i in range(hissi_maara):
            hissi = Hissi(alkerros, ylkerros)
            self.hissit.append(hissi)

    def aja_hissiä(self, hissi_numero, siiry_kerros):

        if hissi_numero in range(len(self.hissit) + 1):

            hissi = self.hissit[hissi_numero - 1]
            hissi.siirry_kerrokseen(siiry_kerros)

        else: 

            print("Sellaista hissiä ei ole olemassa.")

        return


talo = Talo(1, 10, 5)

tulos = talo.aja_hissiä(5, 3)

print(tulos)

tulos = talo.aja_hissiä(2, 6)

print(tulos)

tulos = talo.aja_hissiä(2, 3)

print(tulos)

tulos = talo.aja_hissiä(6, 3)

print(tulos)

for hissi in talo.hissit:

    hissi = hissi.kerros

    print(hissi)
