# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

data = input('Anna luku: ')

while data != "":
   if data.isdigit() == True:
    luku = int(data)
    luvut.insert(0, luku)
    print(luvut) 
    data = input('Anna luku: ')
   else:
    print("Try again") 
    data = input('Anna luku: ')
print("The ptogramm has ended")

pieni = min(luvut)
suuri = max(luvut)

print("Pienin antamasi luku: ", pieni)
print("Suurin antamasi luku ", suuri)