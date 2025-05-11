import random
from hangmankuvat import hangmankuvat         # Tuodaan hirsipuukuvat toisesta tiedostosta

# Esittely ja pelisäännöt
print("Tervetuloa pelaamaan Hirsipuuta!")
print("Arvomme sanan, joka sinun täytyy arvata. Voit arvata max 6 kertaa väärin.")

# Kysytään pelaajalta, onko valmis
oletkovalmis = input("Oletko valmis (kyllä/ei): ")
if oletkovalmis != "kyllä":
    print("Selvä, ehkä myöhemmin.")
    exit()  # Peli ei ala, jos vastaa ei

print("Hienoa! Aloitetaan.")
print("")
print("")

# Sanalista ja satunnainen sanan valinta
sanat = [
    'aurinko',
    'koulu',
    'laivasto',
    'pelastus',
    'kilpikonna',               # pelattavat sanat
    'hylje',
    'rakennus',
    'liikenne',
    'metsästäjä',
    'kamera'
]
sana = random.choice(sanat)     # satunnaisen sanan valinta
arvatut_kirjaimet = ""          # pelaajan arvaamien kirjainten tallennus
yritykset = 6                   # sallittujen väärien vastausten määrä

# pelisilmukka jatkuu, kunnes sana arvattu tai yritykset loppuvat
while yritykset > 0:
    arvaustilanne = ""          # näytetään sana piilotetuilla kirjaimilla
    
    # käydään läpi joka kirjain ja rakennetaan näkyvä versio sanasta
    i = 0
    while i < len(sana):
        if sana[i] in arvatut_kirjaimet:
            arvaustilanne += sana[i]        # näytetään arvattu kirjain
        else:
            arvaustilanne += "_"            # piilotetaan arvaamaton kirjain
        i += 1

    # Tulostetaan nykyinen tilanne
    print("Sana:", arvaustilanne)

    # Peli on voitettu, jos ei ole enää piilotettuja kirjaimia
    if "_" not in arvaustilanne:
        print("Onneksi olkoon! Arvasit sanan!")
        break

    # Näytetään sen hetkinen hirsipuun tilanne
    print(hangmankuvat[6 - yritykset])

    # Pyydetään käyttäjältä kirjain
    kysymys = input("Arvaa kirjain: ").lower()

    # Tarkistetaan, että on vain yksi kirjain
    if len(kysymys) != 1 or not kysymys.isalpha():
        print("Anna vain yksi kirjain kerrallaan.")
        continue

    # Tarkistetaan, onko kirjain jo arvattu
    if kysymys in arvatut_kirjaimet:
        print("Olet jo arvannut kirjaimen", kysymys)
        continue

    # Lisätään kirjain arvattujen listalle
    arvatut_kirjaimet += kysymys

    # Tarkistetaan, onko kirjain oikea vai väärä
    if kysymys in sana:
        print("Oikein!")
    else:
        yritykset -= 1
        print("Väärin! Yrityksiä jäljellä:", yritykset)

# Jos yritykset loppuvat, peli päättyy tappioon
if yritykset == 0:
    print(hangmankuvat[6])  # Näytetään lopullinen hirsipuu
    print("Hävisit! Oikea sana oli:", sana)