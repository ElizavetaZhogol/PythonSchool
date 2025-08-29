# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

luvut = []

arpakuutio = int(input('Anna arpakuutioiden lukumäärä: '))

for n in range(arpakuutio):

    luku = random.randint(1, 6)
    luvut.append(luku)

summa = sum(luvut)

print("Silmälukujen summa on", summa)

