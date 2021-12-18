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

        return Player(row['PLAYERNAME']) if row else None

    def find_all(self):
        """Palauttaa kaikki pelaajanimet.

        Returns:
            Palauttaa listan Player-olioiden pelaajanimistä.
        """

        list_of_names = []
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM PLAYERS')

        rows = cursor.fetchall()

        for name in rows:
            list_of_names.append(name[0])

        return list_of_names

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
            'SELECT * FROM PLAYERS WHERE PLAYERNAME = ?',
            (playername,)
        )

        row = cursor.fetchone()

        return self.get_player_by_row(row)

    def create(self, player):
        """Tallentaa pelaajan tietokantaan.

        Args:
            player: Tallennettava pelaaja Player-oliona.
        Returns:
            Tallennettu pelaaja Player-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO PLAYERS (PLAYERNAME) VALUES (?)',
            (player.playername,)
        )

        self._connection.commit()

        return player

    def delete_all(self):
        """Poistaa kaikki pelaajat.
        """

        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM PLAYERS')

        self._connection.commit()


player_repository = PlayerRepository(get_database_connection())
