# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

tahko = int(input('\nIlmoita noppasi tahkojen yhteismäärä: '))

print("\nKuinka monta nopanheittoa tarvitaan, jotta saadaan luku",tahko,"?\n")

def noppa(tahkot):
    arvo = random.randint(1, tahkot)
    return arvo

luku = noppa(tahko)

n = 1

while luku != tahko:
    print("Numero", luku, "tuli esiin")
    n = n + 1
    luku = noppa(tahko)
else: 
   print("Noppa antoi numero", tahko)

print("Se vaati", n ,"yritystä") 