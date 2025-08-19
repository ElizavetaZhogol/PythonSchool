# Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi.
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input('\nHaluatko tietää, onko vuosi karkausvuosi vai ei? Anna vuosi: '))

if vuosi % 100 == 0:
  if vuosi % 400 == 0:
    print("\n", vuosi, "on karkausvuosi\n")
  else:
    print("\n", vuosi, "ei ole karkausvuosi\n")
elif vuosi % 100 != 0:
  if vuosi % 4 == 0:
    print("\n", vuosi, "on karkausvuosi\n")
  else:
    print("\n", vuosi, "ei ole karkausvuosi\n")  
else: 
  print("\nVirheellinen arvo syötetty\n")
