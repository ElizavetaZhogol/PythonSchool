# Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
# Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

kanta = int(input('Anna suorakulmion kanta: '))
korkeus = int(input('Anna suorakulmion korkeus: '))

piiri = 2*(kanta + korkeus)
pintaAla = kanta*korkeus

print("Suorakulmion kanta on: ", kanta, "\n"
      "Suorakulmion korkeus on: ", korkeus, "\n"
      "Suorakulmion piiri on: ", piiri, "\n" +
      "Suorakulmion pinta-ala on: ", pintaAla)