# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def listSumma(list):
    summa = sum(list)
    return summa

luvut1 = [1, 2, 3, 4, 5]
luvut2 = [6, 7, 8, 9, 10]

tulos1 = listSumma(luvut1)
tulos2 = listSumma(luvut2)

print("Lukujen", luvut1 ,"summa on:", tulos1)
print("Lukujen", luvut2 ,"summa on:", tulos2)

