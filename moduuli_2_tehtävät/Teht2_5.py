# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

# Yksi leiviskä on 20 naulaa.
# Yksi naula on 32 luotia.
# Yksi luoti on 13,3 grammaa.
# Esimerkki ohjelman toiminnasta:

leiviska = float(input('Anna leiviskät: '))
naula = float(input('Anna naulat: '))
luoti = float(input('Anna luodit: '))

leiviskaInGr = leiviska*20*32*13.3 
naulaGrInGr = naula*32*13.3
luotiInGR = luoti*13.3

summaInGr = leiviskaInGr + naulaGrInGr + luotiInGR

killogrammat = summaInGr//1000
grammat = summaInGr%1000

print (f"Massa nykymittojen mukaan: \n {killogrammat:.0f} kilogrammaa {grammat:.2f} grammaa.")

