from entities.player import Player
from connect_database import get_database_connection


class PlayerRepository:
    """Pelaajiin liittyvistä tietokantaoperaatioista vastaava luokka.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden Connection-olio
        """

        self._connection = connection

    def get_player_by_row(self, row):
        """Palauttaa kaikki rivit Player-olioista

        Args:
            row: Rivi, jota haetaan tietokannasta.
        Returns:
            Player-olio, jos pelaajanimen omaava pelaaja on tietokannassa.
            Jos pelaajaa ei ole, palautetaan None.
        """

        return Player(row['playername']) if row else None

    def find_all_names(self):
        """Palauttaa kaikki pelaajanimet.

        Returns:
            Palauttaa listan pelaajanimistä.
        """

        list_of_names = []
        cursor = self._connection.cursor()

        cursor.execute('SELECT playername FROM players')

        rows = cursor.fetchall()

        for name in rows:
            list_of_names.append(name[0])

        return list_of_names

    def find_all(self):
        """Palauttaa kaikki pelaajanimet ja niihin liittyväy pisteet.

        Returns:
            Palauttaa listan pelaajanimistä ja niihin liittyvistä pisteistä.
        """

        list_of_players = []
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM players ORDER BY points DESC')

        rows = cursor.fetchall()

        for player in rows:
            list_of_players.append(player[0])
            list_of_players.append(str(player[1]))

        return list_of_players

    def find_by_playername(self, playername):
        """Palauttaa pelajaajan pelaajanimen perusteella.

        Args:
            playername: Pelaajanimi, jonka pelaaja palautetaan.
        Returns:
            Player-olio, jos pelaajanimen omaava pelaaja on tietokannassa.
            Jos pelaajaa ei ole, palautetaan None.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM players WHERE playername = ?',
            (playername,)
        )

        row = cursor.fetchone()

        return self.get_player_by_row(row)

    def find_points(self, playername):
        """Palauttaa pelaajanimeen liittyvät pisteet.

        Args:
            playername: Pelaajanimi, jonka pisteet palautetaan.
        Returns:
            Kokonaislukuarvo halutun pelaajanimen pisteistä.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT points FROM players WHERE playername = ?',
            (playername,)
        )

        row = cursor.fetchone()

        return int(row[0])

    def update_points(self, player, points):
        """Päivittää tietokantaan halutut pisteet halutulle pelaajanimelle.

        Args:
            player: Pelaajanimi, jonka pisteitä halutaan päivittää.
            points: Pistemäärä, joka vaihdetaan edellisten pisteiden tilalle.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'UPDATE players SET points = ? WHERE playername = ?',
            (points, player,)
        )

        self._connection.commit()

    def create(self, player):
        """Tallentaa pelaajan tietokantaan.

        Args:
            player: Tallennettava pelaaja Player-oliona.
        Returns:
            Tallennettu pelaaja Player-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO players (playername, points) VALUES (?, 0)',
            (player.playername,)
        )

        self._connection.commit()

        return player

    def delete_all(self):
        """Poistaa kaikki pelaajat.
        """

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM players')

        self._connection.commit()


player_repository = PlayerRepository(get_database_connection())
