# Arkkitehtuurikuvaus

## Rakenne

![Pakkausrakenne](./kuvat/arkkitehtuuri_pakkauskaavio.png)

## Päätoiminnallisuudet

### Nopanheittokierros

Esimerkki siitä, miten nopanheittokierros toimii:

![Heittokierros](./kuvat/sekvenssikaavio_kierros.png)

Pelaaja heittää ensin viittä noppaa kerran. Sen jälkeen hän valitsee, mitkä nopista haluaa pitää ja mitä heittää uudelleen. Pelaaja heittää haluamiaan noppia uudelleen. Uudelleen heitetyt nopat lisätään niihin noppiin, jotka ensimmäisellä kierroksella valittiin. Kaikista nopista pelaaja valitsee, mitä noppia hän haluaa käyttää pisteidenlaskussa. Sovelluslogiikkaa tarkistaa mitä mahdollisia vaihtoja pelaajalla on valitsemiensa noppien perusteella ja näyttää kyseiset vaihtoehdot. Pelaaja valitsee näistä yhden ja vaihtoehdon perusteella laskettavat pisteet kirjautuvat tauluun. Tämän jälkeen peli jatkuu uudella kierroksella.
