# Yatzy

<i>Sovellus tehdään Helsingin Yliopiston kurssilla "Ohjelmistotekniikka".</i>

Sovelluksen avulla käyttäjän on mahdollista pelata legendaarista Yatzy-peliä!

## Dokumentaatio

- [Vaatimusmäärittely](./yatzy-app/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpto](./yatzy-app/dokumentaatio/tyoaikakirjanpito.png)
- [Arkkitehtuuri](./yatzy-app/dokumentaatio/arkkitehtuuri.md)

## Asennus

Asenna python3, pip sekä poetry komennoilla:

```
python3
```
```
pip3
```
```
poetry install
```

### Ohjelman suorittaminen

Ohjelma alustetaan komennolla:

```bash
poetry run invoke build
```

Ohjelman suoritus alkaa komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit komennolla:

```bash
poetry run invoke test
```

### Testikattavuusraportti

Raportti testien kattavuudesta saadaan komennoilla:

```
poetry run invoke coverage
poetry run invoke coverage-report
```
Raportti löytyy _htmlcov_-hakemistosta.

### Pylint

Pylintin tarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```

### Jos käytät yliopiston konetta

Käytä komentoja ennen poetryn asentamista ja ohjelman käynnistämistä:
```
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
source $HOME/.poetry/env
```
Muista muokata pyproject.toml tiedostossa pythonin versioksi 3.6.!
