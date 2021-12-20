from sqlite3.dbapi2 import Error
from tkinter import messagebox
from entities.player import Player
from repositories.player_repository import (
    player_repository as default_player_repository)


class PlayerService:
    """Pelaajiin liittyvästä sovelluslogiikasta vastaava luokka."""

    def __init__(self, player_repository=default_player_repository):
        """Luokan konstruktori.  Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            player_repository:
                Vapaaehtoinen, oletusarvoltaan PlayerRepository-olio.
                Olio, jolla on PlayerRepository-luokan metodit.
        """

        self._player = None
        self._player_repository = player_repository

    def create_player(self, playername):
        """Luo uuden pelaajan.

        Args:
            playername: Merkkijonoarvo, joka kuvastaa pelaajan nimimerkkiä.
        Raises:
            Error: Virhe, joka nousee, kun pelaajan nimimerkki on jo käytössä.
        Returns:
            Luotu pelaaja Player-olion muodossa.
        """

        existing_player = self._player_repository.find_by_playername(
            playername)

        if existing_player:
            messagebox.showerror('Error', 'Player name already in use')
            raise Error('Player name already in use')

        self._player = self._player_repository.create(Player(playername))

        return self._player

    def get_all_players(self):
        """Palauttaa kaikki pelaajanimet.

        Returns:
            Merkkijonolistan, joka sisältää kaikki tietokannan pelaajanimet.
        """

        return self._player_repository.find_all_names()

    def get_all_players_and_points(self):
        """Palauttaa kaikki pelaajanimet ja näiden pisteet.

        Returns:
            Merkkijonolistan, joka sisältää kaikki tietokannan pelaajanimet ja pisteet.
        """

        return self._player_repository.find_all()

    def get_points_of_player(self, playername):
        """Palauttaa halutun pelaajanimen pisteet.

        Args:
            playername: Merkkijonoarvo, joka kuvastaa pelaajan nimimerkkiä.
        Returns:
            Haluttuun playername:en liittyvät pisteet.
        """
        return self._player_repository.find_points(playername)

    def update_points(self, playername, points):
        """Vaihtaa halutun pelaajanimen pisteet halutuiksi pisteiksi.

        Args:
            playername: Merkkijonoarvo, joka kuvastaa pelaajan nimimerkkiä.
            points: Kokonaislukuarvo, joka kuvastaa pisteitä,
            jotka vaihdetaan aikaisempien pisteiden tilalle.
        """

        self._player_repository.update_points(playername, points)


player_service = PlayerService()
