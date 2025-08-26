# Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

import getpass

kayttajatunnus = getpass.getuser()
print(kayttajatunnus)

salasana = getpass.getpass('Anna salasana: ')
print(salasana)

print("Kirjaudu tilillesi antamalla käyttäjätunnuksesi ja salasanasi")

tilitunnus = input('Anna käyttäjätunnus')
tilisalasana = input('Anna salasana')

if kayttajatunnus == tilitunnus and salasana == tilisalasana:
    print("Olet kirjautunut tilillesi onnistuneesti.")
elif kayttajatunnus != tilitunnus or salasana != tilisalasana:
    tries = 1
    while tries < 5:
        attempts = 5 - tries
        print("Yritä uudelleen. Sinulla on", attempts, "yritystä jäljellä.")
        tilitunnus = input('Anna käyttäjätunnus')
        tilisalasana = input('Anna salasana')
        if kayttajatunnus == tilitunnus and salasana == tilisalasana:
            print("Olet kirjautunut tilillesi onnistuneesti.")
            break
        else:
            tries = tries + 1

