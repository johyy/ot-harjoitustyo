# Yatzy

<i>Sovellus tehdään Helsingin Yliopiston kurssilla "Ohjelmistotekniikka".</i>

Sovelluksen avulla käyttäjän on mahdollista pelata legendaarista Yatzy-peliä! Peli on yksinpeli, jossa pelaaja heittää viittä noppaa kahdella kierroksella ja päättää sen jälkeen, miten haluaa pisteet käyttää. Tarkoituksena on kerätä mahdollisimman iso pistepotti!

## Dokumentaatio

- [Vaatimusmäärittely](./yatzy-app/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./yatzy-app/dokumentaatio/tyoaikakirjanpito.md)
- [Arkkitehtuuri](./yatzy-app/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](./yatzy-app/dokumentaatio/kayttoohje.md)
- [Releaset](https://github.com/johyy/ot-harjoitustyo/releases)

## Asennus

Poetryn riippuvuudet saadaan asennettua komennolla:

```bash
poetry install
```

Ohjelman tietokannan saa alustettua komennolla:


```bash
poetry run invoke build
```

Itse peli käynnistyy komennolla:


```bash
poetry run invoke start
```

## Komentorivikomennot

### Ohjelman suorittaminen

Ohjelma voidaan suorittaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit komennolla:

```bash
poetry run invoke test
```

### Testikattavuusraportti

Raportti testien kattavuudesta saadaan komennolla:

```
poetry run invoke coverage-report
```
Raportti löytyy _htmlcov_-hakemistosta.


### Pylint

Pylintin tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```

### Jos käytät yliopiston konetta

Käytä komentoja ennen ohjelman käynnistämistä:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
```
