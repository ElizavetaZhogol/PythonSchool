# Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
# Tehtävässä on käytettävä if/elif/else-toistorakennetta.

# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
# C on ikkunaton hytti autokannen alapuolella.
# Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

print ("Valitse laivan hyttiluokka, josta olet kiinnostunut!\n\n"
       "LUX\n"
       "A\n"
       "B\n"
       "C\n")

hyttiluokka = input('Tee valintasi, ilmoita laivan hyttiluokan nimi tähän: ')

if hyttiluokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")