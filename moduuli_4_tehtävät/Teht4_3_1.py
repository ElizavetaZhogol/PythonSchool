# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

# Yksinkertainen ratkaisu, joka ei ota huomioon sitä, että käyttäjä voi syöttää minkä tahansa muun arvon numeron sijaan.

data = input('Anna luku: ')

pieni = 0
suuri = 0

while data != "":
   
   luku = int(data)

   if pieni == 0 and suuri == 0:
      pieni = luku
      suuri = luku
   else:
      if luku > suuri:
        suuri = luku
      elif luku < pieni:
        pieni = luku

   data = input('Anna luku: ')

print("Ohjelma on ohi")


print("Pienin antamasi luku: ", pieni)
print("Suurin antamasi luku ", suuri)