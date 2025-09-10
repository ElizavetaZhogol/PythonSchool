# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='elizavetazhogol',
    password='**********',
    autocommit=True
    )

def lentoasema(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

print("\nSelvitä kahden lentokentän välinen etäisyys.")

icaoKoodi1 = input("\nAnna 1 lentoaseman ICAO-koodi: ")
icaoKoodi2 = input("\nAnna 2 lentoaseman ICAO-koodi: ")

koordinaatti1 = lentoasema(icaoKoodi1)
koordinaatti2 = lentoasema(icaoKoodi2)

etaisyys = distance.distance(koordinaatti1, koordinaatti2).km

print("\nEtäisyys "+ icaoKoodi1 +" lentoaseman ja "+ icaoKoodi2 +" lentoaseman välillä on", etaisyys, "km\n")