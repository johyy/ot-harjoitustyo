from entities.player import Player
from connect_database import get_database_connection


class PlayerRepository:

    def __init__(self, connection):
        self._connection = connection

    def get_player_by_row(self, row):
        return Player(row['PLAYERNAME']) if row else None

    def find_all(self):
        list_of_names = []
        cursor = self._connection.cursor()

        cursor.execute('SELECT * FROM PLAYERS')

        rows = cursor.fetchall()

        for name in rows:
            list_of_names.append(name[0])

        return list_of_names

    def find_by_playername(self, playername):
        cursor = self._connection.cursor()

        cursor.execute(
            'SELECT * FROM PLAYERS WHERE PLAYERNAME = ?',
            (playername,)
        )

        row = cursor.fetchone()

        return self.get_player_by_row(row)

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
