# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

print("\nTietokone arvasi luvun 1-10, yritä arvata!\n")

tietokoneLuku = random.randint(1, 10)
pelaajaLuku = int(input('Anna luku 1-10: '))

while tietokoneLuku != pelaajaLuku:
    if tietokoneLuku > pelaajaLuku:
        print("Liian pieni arvaus")
        pelaajaLuku = int(input('Anna luku 1-10: '))
    elif tietokoneLuku < pelaajaLuku:
        print("Liian suuri arvaus")
        pelaajaLuku = int(input('Anna luku 1-10: '))
    else:
        break
print("\nOikein")
print("Tietokone arvasi numeron", tietokoneLuku, "\n"
      "Arvasit numeron", pelaajaLuku )