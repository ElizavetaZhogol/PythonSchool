# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.

# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

luvut = []

luku = int(input('Anna kokonaisluku: '))

if luku == 2 or luku == 3 or luku == 5:
    print(luku, "on alkuluku!")
else:
    if luku % 2 == 0 or luku % 3 == 0 or luku % 5 == 0:
        print("luku ei ole alkuluku")
