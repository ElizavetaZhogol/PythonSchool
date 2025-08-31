# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

print("\nKuinka monta nopanheittoa tarvitaan, jotta saadaan luku 6?\n")

def noppa():
    arvo = random.randint(1, 6)
    return arvo

luku = noppa()

n = 1

while luku != 6:
    print("Numero", luku, "tuli esiin")
    n = n + 1
    luku = noppa()
else: 
   print("Noppa antoi numero 6")

print("Se vaati", n ,"yritystä") 