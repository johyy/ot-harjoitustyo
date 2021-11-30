from tkinter import Tk
import unittest
from services.dice import Dice
from services.board import Board


class TestDice(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.dice = [1, 1, 1, 1, 1]
        self.new_dice = Dice(self.root)

    def test_roll_dice(self):
        new_dice = self.new_dice.roll_dice(self.dice)
        self.assertNotEqual((new_dice), [1, 1, 1, 1, 1])

    def test_mix_dice(self):
        new_dice = self.new_dice.mix_dice(self.dice)
        self.assertNotEqual((new_dice), [1, 1, 1, 1, 1])


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.new_board = Board(self.root)
