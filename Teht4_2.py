# Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

print ("\nTämä ohjelma muuntaa tuumat senttimetreiksi.\n"
       "Syötä positiivisia arvoja. Negatiivisen arvon syöttäminen pysähtyy.")

tuumia = float(input('\nAnna arvo tuumina: '))

while tuumia > 0:
    senttimetria = tuumia * 2.54
    print(tuumia, "tuuma = ", senttimetria, "cm")
    tuumia = float(input('\nAnna arvo tuumina: '))
else:
    senttimetria = tuumia * 2.54
    print(tuumia, "tuuma = ", senttimetria, "cm")
    print("\nOhjelma on päättynyt")