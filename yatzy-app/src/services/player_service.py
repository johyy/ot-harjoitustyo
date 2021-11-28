from entities.player import Player
from repositories.player_repository import (
    player_repository as default_player_repository)


class PlayerService:
    def __init__(self, player_repository=default_player_repository):
        self._player = None
        self._player_repository = player_repository

    def create_user(self, playername):
        existing_player = self._player_repository.find_by_playername(
            playername)

        if existing_player:
            pass

        player = self._player_repository.create(Player(playername))

        return player

    def in_use(self, playername):
        player = self._player_repository.find_by_playername(playername)

        if not player:
            pass

        self._player = player

        return player

    def get_current_player(self):
        return self._player


player_service = PlayerService()
