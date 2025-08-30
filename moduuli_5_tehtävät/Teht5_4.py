# Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
# (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

for n in range(5):
    kaupunki = input('Anna kaupungin nimi: ')
    kaupungit.append(kaupunki)

print("\nOlet syöttänyt seuraavat kaupungit:\n")

for kaupunki in kaupungit:
    print(kaupunki)
