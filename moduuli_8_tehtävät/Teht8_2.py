# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='elizavetazhogol',
    password='**********',
    autocommit=True
    )

def lentokentta(maakoodi):
    sql = f"SELECT type FROM airport WHERE iso_country = '{maakoodi}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

koodi = input("\nAnna maakoodi (esimerkiksi FI): ")

tyypit = lentokentta(koodi)

# Selvitin tietokannasta kaikenlaiset lentokenttien tyypit kyselyllä:
# select distinct type from airport;

heliport = 0
small_airport = 0
closed = 0
seaplane_base = 0
balloonport = 0
medium_airport = 0
large_airport = 0

for tyyppi in tyypit:

    kenttaTyypi = tyyppi[0]

    if kenttaTyypi == "heliport":
        heliport = heliport + 1
    elif kenttaTyypi == "small_airport":
        small_airport = small_airport + 1
    elif kenttaTyypi == "closed":
        closed = closed + 1
    elif kenttaTyypi == "seaplane_base":
        seaplane_base = seaplane_base + 1
    elif kenttaTyypi == "balloonport":
        balloonport = balloonport + 1
    elif kenttaTyypi == "medium_airport":
        medium_airport = medium_airport + 1
    elif kenttaTyypi == "large_airport":
        large_airport = large_airport + 1

print("\n" + koodi + " maassa on\n" \
"Helikopterikentät: ", heliport, "\n" \
"Pienet lentokentät: ", small_airport, "\n" \
"Suljettu: ", closed, "\n" \
"Vesilentokoneiden tukikohdat: ", seaplane_base, "\n" \
"Ilmapalloportit: ", balloonport, "\n" \
"Keskikokoiset lentokentät: ", medium_airport, "\n" \
"Suuret lentokentät: ", large_airport)