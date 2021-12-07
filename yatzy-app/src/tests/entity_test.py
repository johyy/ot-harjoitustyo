import unittest
from entities.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.new_player = Player("player")

    def test_player(self):
        self.assertEqual((self.new_player.playername), "player")
