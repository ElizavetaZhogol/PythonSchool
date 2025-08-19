# Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

luku1 = int(input('Anna 1 kokonaisluku: '))
luku2 = int(input('Anna 2 kokonaisluku: '))
luku3 = int(input('Anna 3 kokonaisluku: '))

summa = luku1 + luku2 + luku3 
tulo = luku1*luku2*luku3
keskiarvo = (luku1 + luku2 + luku3)/3

print("Luvut: ", luku1, luku2, luku3, "\n"
      "Lukujen summa: ", summa, "\n"
      "Lukujen tulo: ", tulo, "\n"
      "Lukujen keskiarvo: ", keskiarvo)