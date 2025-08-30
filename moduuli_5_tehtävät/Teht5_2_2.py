# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

# Muunnos, jossa ohjelma ei pysähdy, kun syötetään virheellinen arvo

luvut = []

data = input('Ohjelma kysyy numeroita. Ohjelman pysäyttämiseksi paina "Enter". Anna luku: ')

while data != "":

    try:
        luku = int(data)
        luvut.append(luku) 
    except ValueError:
        print("Yritä uudelleen") 

    data = input('Anna luku: ')

if len(luvut) >= 5:
    luvut.sort(reverse = True)
    print("5 suurinta antamaasi arvoa:", luvut[:5])
elif len(luvut) == 0:
    print("Et ole syöttänyt mitään tietoja.")
else:
    luvut.sort(reverse = True)
    arvo = len(luvut)
    print(arvo, "suurinta antamaasi arvoa:", luvut[:arvo])

