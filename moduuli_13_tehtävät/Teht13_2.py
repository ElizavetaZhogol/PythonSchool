# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask
import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port= 3306,
    database='flight_game',
    user='elizavetazhogol',
    password='*****',
    autocommit=True
    )

def lentoasema(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos

app = Flask(__name__)
@app.route('/kenttä/<string:icao>')
def lentokenttä_kaupunki(icao):
        
    result = lentoasema(icao)

    response = {
        "ICAO" : icao,
        "Name" : result[0],
        "Municipality" : result[1]
    }

    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

