# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

def yksikkoHinta(halkaisija, hinta):
    sade = halkaisija/2
    pintaAla = 3.14*sade**2
    pintaAlaMetri = pintaAla/1000
    hintaPerNeliometri = hinta/pintaAlaMetri
    return hintaPerNeliometri

halkaisija1 = float(input('\nAnna 1 pizzan halkaisija cm: '))
hinta1 = float(input('Anna 1 pizzan hinta euroina: '))

halkaisija2 = float(input('\nAnna 2 pizzan halkaisija: '))
hinta2 = float(input('Anna 2 pizzan hinta euroina: '))

yksikkohinta1 = yksikkoHinta(halkaisija1, hinta1)
yksikkohinta2 = yksikkoHinta(halkaisija2, hinta2)

print(f"\nEnsimmäisen pizzan hinta neliömetriltä {yksikkohinta1:.2f} euro/m^2")
print(f"\nToisen pizzan hinta neliömetriltä {yksikkohinta2:.2f} euro/m^2")

if yksikkohinta1 < yksikkohinta2:
    print("\nEnsimmäinen pizza antaa paremman vastineen rahalle!")
elif yksikkohinta1 > yksikkohinta2:
    print("\nToinen pizza antaa paremman vastineen rahalle!")
else:
    print("\nHinta euroina neliömetriltä on sama molemmille pizzoille.")