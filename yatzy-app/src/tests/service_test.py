import unittest
from services.dice import Dice
from services.board import Board


class TestDice(unittest.TestCase):

    def setUp(self):
        self.new_dice = Dice()
        self.dice = [1, 1, 1, 1, 1]

    def test_roll_dice(self):
        new_dice = self.new_dice.roll_dice(self.dice)
        self.assertNotEqual((new_dice), [1, 1, 1, 1, 1])

    def test_mix_dice(self):
        dice = [1, 1, 1]
        other_dice = [2, 2]
        new_dice = self.new_dice.mix_dice(dice, other_dice)
        self.assertEqual((new_dice), [1, 1, 1, 2, 2])

    def test_mix_dice_no_dice(self):
        other_dice = []
        new_dice = self.new_dice.mix_dice(self.dice, other_dice)
        self.assertEqual((new_dice), [1, 1, 1, 1, 1])

    def test_dice_total(self):
        sum = self.new_dice.dice_total(self.dice)
        self.assertEqual((sum), 5)


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.new_board = Board()
        self.dice = [1, 2, 3, 4, 5]

    def test_check_aces_with_aces(self):
        self.assertTrue(self.new_board.check_aces(self.dice))

    def test_check_aces_with_no_aces(self):
        dice = [2, 2, 3, 4, 5]
        self.assertFalse(self.new_board.check_aces(dice))

    def test_check_twos_with_twos(self):
        self.assertTrue(self.new_board.check_twos(self.dice))

    def test_check_twos_with_no_twos(self):
        dice = [1, 1, 3, 4, 5]
        self.assertFalse(self.new_board.check_twos(dice))

    def test_check_threes_with_threes(self):
        self.assertTrue(self.new_board.check_threes(self.dice))

    def test_check_threes_with_no_threes(self):
        dice = [1, 2, 4, 4, 5]
        self.assertFalse(self.new_board.check_threes(dice))

    def test_check_fours_with_fours(self):
        self.assertTrue(self.new_board.check_fours(self.dice))

    def test_check_fours_with_no_fours(self):
        dice = [1, 2, 3, 5, 5]
        self.assertFalse(self.new_board.check_fours(dice))

    def test_check_fives_with_fives(self):
        self.assertTrue(self.new_board.check_fives(self.dice))

    def test_check_fives_with_no_fives(self):
        dice = [1, 2, 3, 4, 4]
        self.assertFalse(self.new_board.check_fives(dice))

    def test_check_sixes_with_sixes(self):
        dice = [2, 3, 4, 5, 6]
        self.assertTrue(self.new_board.check_sixes(dice))

    def test_check_sixes_with_no_sixes(self):
        self.assertFalse(self.new_board.check_sixes(self.dice))

    def test_check_three_kind_with_three_same(self):
        dice = [1, 1, 1, 2, 3]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_no_three_same(self):
        self.assertFalse(self.new_board.check_three_kind(self.dice))

    def test_check_four_kind_with_four_same(self):
        dice = [1, 1, 1, 1, 3]
        self.assertTrue(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_no_four_same(self):
        self.assertFalse(self.new_board.check_four_kind(self.dice))

    def test_full_house_with_full_house(self):
        dice = [1, 1, 1, 2, 2]
        self.assertTrue(self.new_board.check_full_house(dice))

    def test_check_full_house_with_no_full_house(self):
        self.assertFalse(self.new_board.check_full_house(self.dice))

    def test_check_small_straight_with_small_straight(self):
        self.assertTrue(self.new_board.check_small_straight(self.dice))

    def test_check_small_straight_with_no_small_straight(self):
        dice = [1, 1, 2, 3, 4]
        self.assertFalse(self.new_board.check_small_straight(dice))

    def test_check_large_straight_with_large_straight(self):
        dice = [2, 3, 4, 5, 6]
        self.assertTrue(self.new_board.check_large_straight(dice))

    def test_check_large_straight_with_no_large_straight(self):
        self.assertFalse(self.new_board.check_large_straight(self.dice))

    def test_check_yatzy_with_yatzy(self):
        dice = [1, 1, 1, 1, 1]
        self.assertTrue(self.new_board.check_yatzy(dice))

    def test_check_yatzy_with_no_yatzy(self):
        self.assertFalse(self.new_board.check_yatzy(self.dice))

    def test_aces_with_one_ace(self):
        self.assertEqual(self.new_board.aces(self.dice), 1)

    def test_twos_with_one_two(self):
        self.assertEqual(self.new_board.twos(self.dice), 2)

    def test_threes_with_one_three(self):
        self.assertEqual(self.new_board.threes(self.dice), 3)

    def test_fours_with_one_four(self):
        self.assertEqual(self.new_board.fours(self.dice), 4)

    def test_fives_with_one_five(self):
        self.assertEqual(self.new_board.fives(self.dice), 5)

    def test_sixes_with_one_six(self):
        dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.new_board.sixes(dice), 6)

    def test_three_same_with_three_dice(self):
        dice = [1, 1, 1]
        self.assertEqual(self.new_board.three_same(dice), 3)

    def test_three_same_with_four_dice(self):
        dice = [1, 1, 1, 1]
        self.assertEqual(self.new_board.three_same(dice), 3)

    def test_three_same_with_five_dice(self):
        dice = [1, 1, 1, 1, 1]
        self.assertEqual(self.new_board.three_same(dice), 3)
