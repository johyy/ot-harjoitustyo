from tkinter import Tk
import unittest
from services.dice import Dice
class TestDice(unittest.TestCase):

    def setUp(self):
        self.root = Tk()
        self.dice = [1,1,1,1,1]
        self.new_dice = Dice(self.root)

    def test_roll_dice(self):
        new_dice = self.new_dice.roll_dice(self.dice)
        self.assertNotEqual((new_dice), [1,1,1,1,1])