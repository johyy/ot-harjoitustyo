from connect_database import get_database_connection
from entities.player import Player


def get_player_by_row(row):
    return Player(row['PLAYERNAME']) if row else None


class PlayerRepository:

    def __init__(self, connection):
        self._connection = connection

    def find_all(self):
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM PLAYERS')

        rows = cursor.fetchall()

        return list(rows)

    def find_by_playername(self, playername):
        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM PLAYERS WHERE PLAYERNAME = ?',
            (playername,)
        )

        row = cursor.fetchone()

        return get_player_by_row(row)

    def create(self, player):
        cursor = self._connection.cursor()

        cursor.execute(
            'INSERT INTO PLAYERS (PLAYERNAME) VALUES (?)',
            (player.playername,)
        )

        self._connection.commit()

        return player

    def delete_all(self):
        cursor = self._connection.cursor()

        cursor.execute('DELETE FROM PLAYERS')

        self._connection.commit()


player_repository = PlayerRepository(get_database_connection())
