import unittest
from entities.player import Player
from services.dice import Dice
from services.board import Board
from services.player_service import PlayerService
from repositories.player_repository import (
    player_repository as default_player_repository)


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

    def test_check_numbers_with_ace(self):
        self.assertTrue(self.new_board.check_numbers(self.dice, 1))

    def test_check_numbers_with_no_aces(self):
        dice = [2, 2, 3, 4, 5]
        self.assertFalse(self.new_board.check_numbers(dice, 1))

    def test_check_numbers_with_two(self):
        self.assertTrue(self.new_board.check_numbers(self.dice, 2))

    def test_check_numbers_with_no_twos(self):
        dice = [1, 1, 3, 4, 5]
        self.assertFalse(self.new_board.check_numbers(dice, 2))

    def test_check_numbers_with_three(self):
        self.assertTrue(self.new_board.check_numbers(self.dice, 3))

    def test_check_numbers_with_no_threes(self):
        dice = [1, 2, 4, 4, 5]
        self.assertFalse(self.new_board.check_numbers(dice, 3))

    def test_check_numbers_with_four(self):
        self.assertTrue(self.new_board.check_numbers(self.dice, 4))

    def test_check_numbers_with_no_fours(self):
        dice = [1, 2, 3, 5, 5]
        self.assertFalse(self.new_board.check_numbers(dice, 4))

    def test_check_numbers_with_five(self):
        self.assertTrue(self.new_board.check_numbers(self.dice, 5))

    def test_check_numbers_with_no_fives(self):
        dice = [1, 2, 3, 4, 4]
        self.assertFalse(self.new_board.check_numbers(dice, 5))

    def test_check_numbers_with_six(self):
        dice = [2, 3, 4, 5, 6]
        self.assertTrue(self.new_board.check_numbers(dice, 6))

    def test_check_numbers_with_no_sixes(self):
        self.assertFalse(self.new_board.check_numbers(self.dice, 6))

    def test_check_three_kind_with_three_same(self):
        dice = [3, 1, 1, 1, 3]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_no_three_same(self):
        self.assertFalse(self.new_board.check_three_kind(self.dice))

    def test_check_three_kind_with_three_dice(self):
        dice = [1, 1, 1]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_four_dice(self):
        dice = [2, 1, 1, 1]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_three_dice_no_same(self):
        dice = [1, 2, 3]
        self.assertFalse(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_five_dice(self):
        dice = [2, 5, 5, 5, 3]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_three_kind_with_five_dice_different_order(self):
        dice = [2, 5, 5, 5, 6]
        self.assertTrue(self.new_board.check_three_kind(dice))

    def test_check_four_kind_with_four_same(self):
        dice = [1, 1, 1, 1, 3]
        self.assertTrue(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_four_same_different_order(self):
        dice = [5, 5, 5, 5, 3]
        self.assertTrue(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_four_dice(self):
        dice = [1, 1, 1, 1]
        self.assertTrue(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_four_dice_not_same(self):
        dice = [1, 2, 3, 1]
        self.assertFalse(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_three_dice(self):
        dice = [1, 1, 1]
        self.assertFalse(self.new_board.check_four_kind(dice))

    def test_check_four_kind_with_no_four_same(self):
        self.assertFalse(self.new_board.check_four_kind(self.dice))

    def test_full_house_with_full_house(self):
        dice = [1, 1, 1, 2, 2]
        self.assertTrue(self.new_board.check_full_house(dice))

    def test_full_house_with_full_house_different_dice(self):
        dice = [1, 1, 2, 2, 2]
        self.assertTrue(self.new_board.check_full_house(dice))

    def test_full_house_with_full_house_false_dice(self):
        dice = [1, 1, 1, 2, 3]
        self.assertFalse(self.new_board.check_full_house(dice))

    def test_full_house_with_full_house_different_false_dice(self):
        dice = [1, 1, 2, 2, 3]
        self.assertFalse(self.new_board.check_full_house(dice))

    def test_check_full_house_with_no_full_house(self):
        self.assertFalse(self.new_board.check_full_house(self.dice))

    def test_check_full_house_with_no_dice(self):
        dice = []
        self.assertFalse(self.new_board.check_full_house(dice))

    def test_check_small_straight_with_small_straight(self):
        self.assertTrue(self.new_board.check_small_straight(self.dice))

    def test_check_small_straight_with_no_small_straight(self):
        dice = [1, 1, 2, 3, 4]
        self.assertFalse(self.new_board.check_small_straight(dice))

    def test_check_small_straight_with_no_dice(self):
        dice = []
        self.assertFalse(self.new_board.check_small_straight(dice))

    def test_check_large_straight_with_large_straight(self):
        dice = [2, 3, 4, 5, 6]
        self.assertTrue(self.new_board.check_large_straight(dice))

    def test_check_large_straight_with_no_large_straight(self):
        self.assertFalse(self.new_board.check_large_straight(self.dice))

    def test_check_large_straight_with_no_dice(self):
        dice = []
        self.assertFalse(self.new_board.check_large_straight(dice))

    def test_check_yatzy_with_yatzy(self):
        dice = [1, 1, 1, 1, 1]
        self.assertTrue(self.new_board.check_yatzy(dice))

    def test_check_yatzy_with_no_yatzy(self):
        self.assertFalse(self.new_board.check_yatzy(self.dice))

    def test_check_yatzy_with_no_dice(self):
        dice = []
        self.assertFalse(self.new_board.check_yatzy(dice))

    def test_numbers_with_one_ace(self):
        self.assertEqual(self.new_board.numbers(self.dice, 1), 1)

    def test_numbers_with_one_two(self):
        self.assertEqual(self.new_board.numbers(self.dice, 2), 2)

    def test_numbers_with_one_three(self):
        self.assertEqual(self.new_board.numbers(self.dice, 3), 3)

    def test_numbers_with_one_four(self):
        self.assertEqual(self.new_board.numbers(self.dice, 4), 4)

    def test_numbers_with_one_five(self):
        self.assertEqual(self.new_board.numbers(self.dice, 5), 5)

    def test_numbers_with_one_six(self):
        dice = [2, 3, 4, 5, 6]
        self.assertEqual(self.new_board.numbers(dice, 6), 6)

    def test_three_same_with_three_dice(self):
        dice = [1, 1, 1]
        self.assertEqual(self.new_board.three_same(dice), 3)

    def test_three_same_with_four_dice(self):
        dice = [1, 1, 1, 1]
        self.assertEqual(self.new_board.three_same(dice), 3)

    def test_three_same_with_four_different_dice(self):
        dice = [1, 2, 2, 2]
        self.assertEqual(self.new_board.three_same(dice), 6)

    def test_three_same_with_four_false_dice(self):
        dice = [1, 2, 2, 3]
        self.assertEqual(self.new_board.three_same(dice), 0)

    def test_three_same_with_five_dice(self):
        dice = [1, 1, 1, 2, 2]
        self.assertEqual(self.new_board.three_same(dice), 3)

    def test_three_same_with_five_dice_different_order(self):
        dice = [1, 3, 3, 3, 4]
        self.assertEqual(self.new_board.three_same(dice), 9)

    def test_three_same_with_five_different_dice(self):
        dice = [1, 2, 3, 3, 3]
        self.assertEqual(self.new_board.three_same(dice), 9)

    def test_three_same_with_five_false_dice(self):
        dice = [1, 2, 2, 3, 4]
        self.assertEqual(self.new_board.three_same(dice), 0)

    def test_three_same_with_no_dice(self):
        dice = []
        self.assertEqual(self.new_board.three_same(dice), 0)

    def test_four_same_with_four_dice(self):
        dice = [1, 1, 1, 1]
        self.assertEqual(self.new_board.four_same(dice), 4)

    def test_four_same_with_four_false_dice(self):
        dice = [1, 1, 2, 1]
        self.assertEqual(self.new_board.four_same(dice), 0)

    def test_four_same_with_five_dice(self):
        dice = [1, 1, 1, 1, 1]
        self.assertEqual(self.new_board.four_same(dice), 4)

    def test_four_same_with_five_different_dice(self):
        dice = [2, 2, 2, 2, 1]
        self.assertEqual(self.new_board.four_same(dice), 8)

    def test_four_same_with_five_false_dice(self):
        dice = [2, 2, 2, 1, 1]
        self.assertEqual(self.new_board.four_same(dice), 0)

    def test_mark_aces_true(self):
        self.assertTrue(self.new_board.mark_aces(self.dice))

    def test_mark_aces_when_ones_are_added(self):
        self.assertFalse(self.new_board.mark_aces(self.dice))

    def test_mark_twos_true(self):
        self.assertTrue(self.new_board.mark_twos(self.dice))

    def test_mark_twos_when_twos_are_added(self):
        self.assertFalse(self.new_board.mark_twos(self.dice))

    def test_mark_threes_true(self):
        self.assertTrue(self.new_board.mark_threes(self.dice))

    def test_mark_threes_when_threes_are_added(self):
        self.assertFalse(self.new_board.mark_threes(self.dice))

    def test_mark_fours_true(self):
        self.assertTrue(self.new_board.mark_fours(self.dice))

    def test_mark_fours_when_fours_are_added(self):
        self.assertFalse(self.new_board.mark_fours(self.dice))

    def test_mark_fives_true(self):
        self.assertTrue(self.new_board.mark_fives(self.dice))

    def test_mark_fives_when_fives_are_added(self):
        self.assertFalse(self.new_board.mark_fives(self.dice))

    def test_mark_sixes_true(self):
        self.assertTrue(self.new_board.mark_sixes(self.dice))

    def test_mark_sixes_when_sixes_are_added(self):
        self.assertFalse(self.new_board.mark_sixes(self.dice))

    def test_mark_three_same_true(self):
        dice = [1, 1, 1, 2, 3]
        self.assertTrue(self.new_board.mark_three_same(dice))

    def test_mark_three_same_when_three_same_are_added(self):
        dice = [1, 1, 1, 2, 3]
        self.assertFalse(self.new_board.mark_three_same(dice))

    def test_mark_four_same_true(self):
        dice = [1, 1, 1, 1, 3]
        self.assertTrue(self.new_board.mark_four_same(dice))

    def test_mark_four_same_when_four_same_are_added(self):
        dice = [1, 1, 1, 1, 3]
        self.assertFalse(self.new_board.mark_four_same(dice))

    def test_mark_full_house_true(self):
        dice = [1, 1, 1, 3, 3]
        self.assertTrue(self.new_board.mark_full_house(dice))

    def test_mark_full_house_when_full_house_is_added(self):
        dice = [1, 1, 1, 3, 3]
        self.assertFalse(self.new_board.mark_full_house(dice))

    def test_mark_small_straight_true(self):
        self.assertTrue(self.new_board.mark_small_straight(self.dice))

    def test_mark_small_straight_when_small_straight_is_added(self):
        self.assertFalse(self.new_board.mark_small_straight(self.dice))

    def test_mark_large_straight_true(self):
        dice = [2, 3, 4, 5, 6]
        self.assertTrue(self.new_board.mark_large_straight(dice))

    def test_mark_large_straight_when_large_straight_is_added(self):
        dice = [2, 3, 4, 5, 6]
        self.assertFalse(self.new_board.mark_large_straight(dice))

    def test_mark_chance_true(self):
        self.assertTrue(self.new_board.mark_chance(self.dice))

    def test_mark_chance_when_chance_is_added(self):
        self.assertFalse(self.new_board.mark_chance(self.dice))

    def test_mark_yatzy_true(self):
        dice = [1, 1, 1, 1, 1]
        self.assertTrue(self.new_board.mark_yatzy(dice))

    def test_mark_yatzy_when_yatzy_is_added(self):
        dice = [1, 1, 1, 1, 1]
        self.assertFalse(self.new_board.mark_yatzy(dice))


class TestPlayerService(unittest.TestCase):

    def setUp(self):
        self.new_player_service = PlayerService(
            player_repository=default_player_repository)
        self.new_player_service._player_repository.delete_all()

    def test_get_current_player_with_none(self):
        self.assertIsNone(self.new_player_service.get_current_player())

    def test_in_use(self):
        self.assertIsNone(self.new_player_service.in_use('Testuri'))

    def test_get_all_players_with_none(self):
        self.assertEqual(self.new_player_service.get_all_players(), [])
