# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

luku = int(input('Anna luku: '))
print(luku)



while type(luku) == int:
    luvut.insert(1, luku)
    print(luvut)
    luku = int(input('Anna luku: '))
    if luku == "":
      print("Error")
      break
else:
    print("invalid input")
#     if luku == "":
#         print("Error")
#         break
#     luku = int(input('Anna luku: '))
# else:
#     print("wrong input")

