# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Yritin tässä kirjoittaa ohjelman, joka ei pysähdy virheellisen arvon syöttämisen vuoksi.
# Koska ohjelman pitäisi pysähtyä vain, kun käyttäjä ei ole syöttänyt mitään.

luvut = []

data = input('Anna luku: ')

while data != "":
   try:
    luku = int(data)
    luvut.insert(0, luku)
    print(luvut) 
   except ValueError:
    print("Yritä uudelleen") 
   data = input('Anna luku: ')
print("Ohjelma on ohi")

pieni = min(luvut)
suuri = max(luvut)

print("Pienin antamasi luku: ", pieni)
print("Suurin antamasi luku ", suuri)