# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31. Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

from flask import Flask, Response 
import json

def alkuluku(number):
    if number < 2:
        return False

    elif number == 2:

        return True
    else: 
        for luku in range(2, number):
            arvo = number % luku
            if arvo == 0:
                return False
        return True

app = Flask(__name__)
@app.route('/alkuluku/<int:number>')
def ilmoittaa_alkuluku(number):
    try:     
        isPrime = alkuluku(number)

        response = {
            "Number" : number,
            "isPrime" : isPrime
        }

        return response
    
    except: 
        response = {
            "message": "Invalid number as addend",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response

@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)