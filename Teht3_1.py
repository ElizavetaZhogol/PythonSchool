# Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

kuhanPituus = float(input('Anna kuhan pituus senttimetreinä: '))

if kuhanPituus >= 37:
    print("Erinomaista kuhaa, ota mukaasi!")
else:
    cmPuuttuu = 37 - kuhanPituus
    print("Kuha on alamittainen. Laske kuhan takaisin järveen! Kuhan on oltava 37 cm pitkä, jotta se pysyy. Sinulta puuttuu", cmPuuttuu, "cm.")    