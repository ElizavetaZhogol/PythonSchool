# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Sama esimerkki min- ja max-funktioiden avulla. Ohjelma ei myöskään ota huomioon käyttäjän syöttämiä tietoja, kuten tekstiä. 

luvut = []

data = input('Anna luku: ')

while data != "":
   
   luku = int(data)
   luvut.insert(0, luku)
   print(luvut) 
   data = input('Anna luku: ')
   
print("Ohjelma on ohi")

pieni = min(luvut)
suuri = max(luvut)

print("Pienin antamasi luku: ", pieni)
print("Suurin antamasi luku ", suuri)