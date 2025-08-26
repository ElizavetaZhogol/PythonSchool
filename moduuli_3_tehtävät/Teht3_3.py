# Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

# Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
# Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input('\nMikä on biologinen sukupuolisi? Kirjoita vastauksesi tähän: ')
hemoglobiiniarvo = int(input("Mikä on hemoglobiiniarvosi? Kirjoita tähän: "))

if sukupuoli == "nainen":

    print("\nOlet " + sukupuoli + ".\n"
      "Hemoglobiiniarvosi on", hemoglobiiniarvo, ".\n")

    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen.\n"
              "Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.\n")
    elif 117<=hemoglobiiniarvo<=175:
        print("Hemoglobiiniarvosi on normaali.\n"
              "Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.\n")
    elif hemoglobiiniarvo > 175:
        print("Hemoglobiiniarvosi on korkea.\n"
              "Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.\n")
        
elif sukupuoli == "mies":

    print("\nOlet " + sukupuoli + ".\n"
      "Hemoglobiiniarvosi on", hemoglobiiniarvo, ".\n")

    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen.\n"
              "Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.\n")
    elif 134<=hemoglobiiniarvo<=195:
        print("Hemoglobiiniarvosi on normaali.\n"
              "Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.\n")
    elif hemoglobiiniarvo > 195:
        print("Hemoglobiiniarvosi on korkea.\n"
              "Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.\n")
else:
    print("Syötit tiedot väärin.\n")