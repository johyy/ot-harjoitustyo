import unittest
from repositories.player_repository import player_repository
from entities.player import Player


class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        player_repository.delete_all()
        self.player_maija_meikalainen = Player('Maija Meikäläinen')
        self.player_matti_meikalainen = Player('Matti Meikäläinen')

    def test_create(self):
        player_repository.create(self.player_maija_meikalainen)
        players = player_repository.find_all()

        self.assertEqual(len(players), 1)
        self.assertEqual(players[0], self.player_maija_meikalainen.playername)

    def test_find_all(self):
        player_repository.create(self.player_maija_meikalainen)
        player_repository.create(self.player_matti_meikalainen)
        players = player_repository.find_all()

        self.assertEqual(len(players), 2)
        self.assertEqual(players[0], self.player_maija_meikalainen.playername)
        self.assertEqual(players[1], self.player_matti_meikalainen.playername)

    def test_find_by_playername(self):
        player_repository.create(self.player_maija_meikalainen)

        player = player_repository.find_by_playername(
            self.player_maija_meikalainen.playername)

        self.assertEqual(player.playername,
                         self.player_maija_meikalainen.playername)
