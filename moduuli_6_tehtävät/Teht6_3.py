# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
# palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def bensiiniLitra(gallonat):
    litra = gallonat*3.785
    return litra

print("Haluatko tietää, kuinka monta litraa bensiiniä on varastossa gallonoina?")

gallona = int(input('Anna gallonien määrä. Ohjelman pysäyttämiseksi anna negatiivinen arvo: '))

while gallona >= 0:
    tulos = bensiiniLitra(gallona)
    print(gallona, f"gallonaa sisältää {tulos:.3f} litraa bensiiniä")
    gallona = int(input('Anna gallonien määrä: '))
else:
    print("Ohjelma on päättynyt")

