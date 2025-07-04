# HANGMAN
Projektina Hangman -peli
Jenna Vahviala ja Tinja Pennanen

### Demo-linkki
Pelin demoon pääsee tästä linkistä:
[esittelyvideot](https://fotovahviala.kuvat.fi/i/9rZXJYF7QtGg3V5dWEUDHe46RkhbPNv8)

### Työmäärän jakautuminen
Työnjako oli seuraava:

Jenna Vahviala:
- README -tiedoston luominen
- Pelilogiikka
- Sanan arvaaminen

Tinja Pennanen:
- Vuokaavion luominen ja liittäminen
- Pelitilanteen näyttäminen
- ASCII-hirsipuu

## Sisällysluettelo:

- [Tietoa pelistä](#tietoa-pelistä)  
- [Kuvakaappaukset](#kuvakaappaukset)  
- [Teknologiat](#teknologiat)    
- [Suunnitelma / Vuokaavio](#suunnittelu)  
- [Aikataulu](#aikataulu)  
- [Lähteet ja tekijät](#lähteet-ja-tekijät)   

## Tietoa pelistä 
Hangman on klassinen sana-arvuuttelupeli, jossa peli arpoo "salasanan", joka pelaajan tulee arvata. Pelissä on varaa kuudelle virheelle ja virheelliset arvausyritykset johtavat hirsipuun piirtämiseen. 

Pelissä pelaaja arvaa kirjaimia yksitellen; jos kirjain on sanassa, kirjain merkitään sanassa oikealle kohdalleen. Jos arvattu kirjain ei ole sanassa, siitä tulee virhe, jonka seurauksena hirsipuu rupeaa valmistumaan. Pelin voittaa, jos arvaa kaikki kirjaimet oikein muodostaen salasanan. Jos yritykset pääsevät loppumaan ja hirsipuu on piirretty loppuun, pelaaja häviää.

## Kuvakaappaukset  
Alla pari kuvaa toimivasta koodista.

[koodikuva1](kuvat/Screenshot1.png)
[koodikuva2](kuvat/Screenshot2.png)

## Teknologiat
Alustana toimi GitHub sekä Visual Studio Code koodin kirjoittamisessa. VS Codessa käytimme Python -ohjelmointikieltä koodin luomiseen. Koodin kirjoittamisessa oli apuna ChatGPT.

## Suunnittelu
Tässä kuva meidän Vuokaaviosta:
[Vuokaavio](kuvat/Vuokaavio1.png)

Halusimme koodata jotain kivaa ja interaktiivista, jossa pelaaja saa itse olla koko ajan mukana. Tekoäly suositteli Hangman -peliä.

1. Pelin peruslogiikan ymmärtäminen
- sääntöjen määrittäminen
- logiikan osat: sanan valinta (satunnaisvalinta), pelaajan syötteet (arvaukset) ja yritykset sekä arvatut kirjaimet

2. Käyttäjän syötteen käsittely
- "käyttöliittymän" suunnittelu
- pelin aloitus: pelataanko vai ei
- syötteen tarkistus: yksi kirjain kerrallaan

3. Pelin kulun logiikka
- sanavalinta satunnaisesti
- Arvausten tarkistus
- pelilogiikka: arvauksia verrataan sanaan

4. Pelin visuaalisuus ja käyttäjäkokemus
- hirsipuu-grafiikka: hirsipuun kuvat eri tiedostossa
- viestit: oikein/väärin, virheelliset syötteet

5. Virheenkäsittely
- useita tarkistuksia
- selkeitä (virhe-)ilmoituksia

6. Pelin lopetus
- selkeä lopetus: voitto vai häviö

7. Uudelleen pelaaminen
- kysymys uudestaan pelaamisesta

## Aikataulu
Projektin alustava aikataulu:

5.5. - Projektin hahmottaminen, idean keksiminen ja README -tiedoston kirjoittaminen  
vko 19 - koodin kirjoittaminen  
vko 20 - koodin kirjoittaminen, tilannekatsaus  
vko 21 - koodin viimeistely  
26.5. - Projektin palautus

## Lähteet ja tekijät  
Lista osallistujista ja lähteistä:

- Jenna Vahviala
- Tinja Pennanen
- ChatGPT
- MOOC teoriat
- Mika Stenberg teoriat tunnilla
