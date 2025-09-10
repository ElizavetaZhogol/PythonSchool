# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen,
# ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

print("\nHaluatko syöttää uuden lentoaseman? Syötä numero 1\n" \
"Haluatko hakea jo syötetyn lentoaseman tiedot? Syötä numero 2\n"  \
"Haluatko lopettaa? Syötä numero 3\n")

lentoasemat = {}

luku = int(input('Syötä valintasi 1, 2 tai 3: '))

while luku != 3:

    if luku == 1:
        icao = input('Anna lentoaseman ICAO-koodi: ')
        nimi = input('Anna lentoaseman nimi: ')

        lentoasemat[icao] = nimi

    elif luku == 2:
        icao = input('Anna lentoaseman ICAO-koodi: ')

        if icao in lentoasemat:
            print(icao + " ICAO:n määräysten mukainen lentoasema on " + lentoasemat[icao])
        else:
            print("Listalla ei ole sellaista lentoasemaa.")

    else:
        print("Ei ole sellaista vaihtoehtoa. Yritä uudelleen.")

    luku = int(input('Syötä valintasi 1, 2 tai 3: '))
