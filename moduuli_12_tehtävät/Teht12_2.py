# Tutustu avoimeen OpenWeather-säärajapintaan: https://openweathermap.org/api.
# Kirjoita ohjelma, joka kysyy käyttäjältä paikkakunnan nimen ja tulostaa sitä vastaavan säätilan tekstin sekä lämpötilan Celsius-asteina.
# Perehdy rajapinnan dokumentaatioon riittävästi.
# Palveluun rekisteröityminen on tarpeen, jotta saat rajapintapyynnöissä tarvittavan API-avaimen (API key).
# Selvitä myös, miten saat Kelvin-asteet muunnettua Celsius-asteiksi.

import requests

paikkakunta = input('\nAnna paikkakunnan nimi selvittääksesi sääolosuhteet: ') 

request = "https://api.openweathermap.org/data/2.5/weather?q=" + paikkakunta +"&appid=be76e954083b11eaf7a611f46924c70d"

try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        
        lämpötila = json_response["main"]["temp"]
        säätila = json_response["weather"][0]["description"]

        celsius = lämpötila - 273.15

        print(f"\nLämpötila paikkakunnassa {paikkakunta} on: {celsius:.0f} astetta.")
        print(f"Sääolosuhteet ovat: {säätila}")

except requests.exceptions.RequestException as e:
    print ("Request could not be completed.")