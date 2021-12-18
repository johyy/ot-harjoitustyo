from sqlite3.dbapi2 import Error
from tkinter import messagebox
from entities.player import Player
from repositories.player_repository import (
    player_repository as default_player_repository)


class PlayerService:
    def __init__(self, player_repository=default_player_repository):
        self._player = None
        self._player_repository = player_repository

    def create_player(self, playername):
        existing_player = self._player_repository.find_by_playername(
            playername)

        if existing_player:
            messagebox.showerror('Error', 'Player name already in use')
            raise Error('Player name already in use')

        self._player = self._player_repository.create(Player(playername))

        return self._player

    def in_use(self, playername):
        player = self._player_repository.find_by_playername(playername)

        if not player:
            pass

        self._player = player

        return player

    def get_current_player(self):
        return self._player

    def get_all_players(self):
        return self._player_repository.find_all()


player_service = PlayerService()
