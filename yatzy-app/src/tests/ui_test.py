import unittest
from tkinter import messagebox
from ui.play_view import PlayView
from ui.add_player_view import PlayersView
from ui.index_view import IndexView

class TestPlayView(unittest.TestCase):
    def setUp(self):
        self.play = PlayView
        self.dice = [1,1,1,1,1]

    def test_show_dice(self):
        self.assertEqual(len(self.dice), 5)

class TestPlayersView(unittest.TestCase):
    def setUp(self):
        self.players = PlayersView
        self._player_entry = None
    
    def test_add_player(self):
        pass
