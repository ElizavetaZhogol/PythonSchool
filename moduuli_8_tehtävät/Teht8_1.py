# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='elizavetazhogol',
    password='HelloElizaveta!_2025',
    autocommit=True
    )

def lentoasema(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

icaoKoodi = input("\nAnna lentoaseman ICAO-koodi: ")

final = lentoasema(icaoKoodi)

print("\n" + icaoKoodi + " ICAO:n-koodin vastaa " + final[0] + ", " + final[1] + " sijaintikunta.\n")