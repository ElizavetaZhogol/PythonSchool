# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luvut = int(input('Anna kokonaisluku: '))

vastaus = "on alkuluku"

for luku in range(2, luvut):
    arvo = luvut % luku
    print(arvo)
    if arvo == 0:
        vastaus = "ei ole alkuluku"
        break

if luvut == 0 or luvut == 1:
    print(luvut, "ei ole alkuluku")
elif luvut < 0:
    print("Anna positiivinen luku")
else:
    print(luvut, vastaus)