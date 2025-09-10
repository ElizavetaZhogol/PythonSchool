# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = ("Talvi", "Kevät", "Kesä", "Syksy")

kuukausiNumero = int(input('\nAnna kuukauden numero (1-12): '))

if kuukausiNumero == 12 or 0 < kuukausiNumero <= 2:
    vuodenaika = vuodenajat[0]
    print("\nKuukausi", kuukausiNumero ,"on " + vuodenaika + " kuukausi")
elif 2 < kuukausiNumero <= 5:
    vuodenaika = vuodenajat[1]
    print("\nKuukausi", kuukausiNumero ,"on " + vuodenaika + " kuukausi")
elif 5 < kuukausiNumero <= 8:
    vuodenaika = vuodenajat[2]
    print("\nKuukausi", kuukausiNumero ,"on " + vuodenaika + " kuukausi")
elif 8 < kuukausiNumero <= 11:
    vuodenaika = vuodenajat[3]
    print("\nKuukausi", kuukausiNumero ,"on " + vuodenaika + " kuukausi")
else:
    print("Tällä numerolla ei ole kuukautta")