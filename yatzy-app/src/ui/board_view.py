from tkinter import *
from tkinter import messagebox
from services.board import Board
from services.player_service import PlayerService


class BoardView:
    "Luokka, joka vastaa pisteiden valinnan ja näytön näkymästä."
    
    def __init__(self, root, player, rolled_dice, sum, handle_play_view):
        self._root = root
        self.rolled_dice = rolled_dice
        self.sum = sum
        self.player = player
        self.handle_play_view = handle_play_view
        self._frame = None
        self.new_board = Board()
        self.player_service = PlayerService()
        self.list = None
        self.board_list = Listbox(self._frame)
        self.question = None
        self.continue_button = None

        self.aces_button = None
        self.twos_button = None
        self.threes_button = None
        self.fours_button = None
        self.fives_button = None
        self.sixes_button = None
        self.three_same_button = None
        self.four_same_button = None
        self.full_house_button = None
        self.small_straight_button = None
        self.large_straight_button = None
        self.chance_button = None
        self.yatzy_button = None
        self.choose_zero_button = None

        self.zero_aces_button = None
        self.zero_twos_button = None
        self.zero_threes_button = None
        self.zero_fours_button = None
        self.zero_fives_button = None
        self.zero_sixes_button = None
        self.zero_three_same_button = None
        self.zero_four_same_button = None
        self.zero_full_house_button = None
        self.zero_small_straight_button = None
        self.zero_large_straight_button = None
        self.zero_chance_button = None
        self.zero_yatzy_button = None

        self._initialize()

    def _initialize(self):
        self._frame = Frame(master=self._root)
        self._frame.grid()
        self.question = Label(
            self._frame, text="How do you want to use these " + str(self.sum) + " points?")
        self.choose_zero_button = Button(
            self._frame, text='Choose this if you want to mark a zero', command=self._zero)

        self.list = Listbox(self._frame)
        i = 0
        while i < len(self.rolled_dice):
            self.list.insert(i, str(self.rolled_dice[i]))
            i += 1
        self.list.grid()
        self.question.grid()

        if self.new_board.check_numbers(self.rolled_dice, 1):
            self.aces_button = Button(
                self._frame, text='Aces', command=self._aces)
            self.aces_button.grid()
        if self.new_board.check_numbers(self.rolled_dice, 2):
            self.twos_button = Button(
                self._frame, text='Twos', command=self._twos)
            self.twos_button.grid()
        if self.new_board.check_numbers(self.rolled_dice, 3):
            self.threes_button = Button(
                self._frame, text='Threes', command=self._threes)
            self.threes_button.grid()
        if self.new_board.check_numbers(self.rolled_dice, 4):
            self.fours_button = Button(
                self._frame, text='Fours', command=self._fours)
            self.fours_button.grid()
        if self.new_board.check_numbers(self.rolled_dice, 5):
            self.fives_button = Button(
                self._frame, text='Fives', command=self._fives)
            self.fives_button.grid()
        if self.new_board.check_numbers(self.rolled_dice, 6):
            self.sixes_button = Button(
                self._frame, text='Sixes', command=self._sixes)
            self.sixes_button.grid()
        if self.new_board.check_three_kind(self.rolled_dice):
            self.three_same_button = Button(
                self._frame, text='3 of a kind', command=self._three_same)
            self.three_same_button.grid()
        if self.new_board.check_four_kind(self.rolled_dice):
            self.four_same_button = Button(
                self._frame, text='4 of a kind', command=self._four_same)
            self.four_same_button.grid()
        if self.new_board.check_full_house(self.rolled_dice):
            self.full_house_button = Button(
                self._frame, text='Full House', command=self._full_house)
            self.full_house_button.grid()
        if self.new_board.check_small_straight(self.rolled_dice):
            self.small_straight_button = Button(
                self._frame, text='Small Straight', command=self._small_straight)
            self.small_straight_button.grid()
        if self.new_board.check_large_straight(self.rolled_dice):
            self.large_straight_button = Button(
                self._frame, text='Large Straight', command=self._large_straight)
            self.large_straight_button.grid()
        self.chance_button = Button(
            self._frame, text='Chance', command=self._chance)
        self.chance_button.grid()
        if self.new_board.check_yatzy(self.rolled_dice):
            self.yatzy_button = Button(
                self._frame, text='Yatzy', command=self._yatzy)
            self.yatzy_button.grid()

        self.choose_zero_button.grid()

    def _roll_dice(self):

        if self.new_board.check_if_full() is True:
            totalsum = self.new_board.count_total()
            if int(totalsum) > self.player_service.get_points_of_player(self.player):
                self.player_service.update_points(self.player, totalsum)
                messagebox.showinfo(
                    'NEW TOP SCORE!', self.player + ' makes history!')
            you_win = messagebox.askquestion(
                self.player + ' wins!', 'You got ' + totalsum + ' points! You should stop playing now.', icon='warning')
            if you_win == 'yes':
                self._root.destroy()
            else:
                messagebox.showinfo(
                    'No more!', 'I mean it. You need to stop playing, ' + self.player + '!')
                self._root.destroy()
        else:
            self._frame.destroy()
            self.handle_play_view(self.player)
            self.board_list.destroy()

    def _aces(self):
        if self.new_board.mark_aces(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have aces")
        else:
            self._show_table()

    def _twos(self):
        if self.new_board.mark_twos(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have twos")
        else:
            self._show_table()

    def _threes(self):
        if self.new_board.mark_threes(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have threes")
        else:
            self._show_table()

    def _fours(self):
        if self.new_board.mark_fours(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have fours")
        else:
            self._show_table()

    def _fives(self):
        if self.new_board.mark_fives(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have fives")
        else:
            self._show_table()

    def _sixes(self):
        if self.new_board.mark_sixes(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have sixes")
        else:
            self._show_table()

    def _three_same(self):
        if self.new_board.mark_three_same(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have three of a kind")
        else:
            self._show_table()

    def _four_same(self):
        if self.new_board.mark_four_same(self.rolled_dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have four of a kind")
        else:
            self._show_table()

    def _full_house(self):
        if self.new_board.mark_full_house(self.sum) == False:
            messagebox.showinfo("Choose something else",
                                "You already have full house")
        else:
            self._show_table()

    def _small_straight(self):
        num = 15
        if self.new_board.mark_small_straight(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have small straight")
        else:
            self._show_table()

    def _large_straight(self):
        num = 20
        if self.new_board.mark_large_straight(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have large straight")
        else:
            self._show_table()

    def _chance(self):
        if self.new_board.mark_chance(self.sum) == False:
            messagebox.showinfo("Choose something else",
                                "You already have chance")
        else:
            self._show_table()

    def _yatzy(self):
        num = 50
        if self.new_board.mark_yatzy(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have yatzy")
        else:
            self._show_table()

    def _zero(self):
        self.zero_aces_button = Button(
            self._frame, text='Aces', command=self._zero_aces)
        self.zero_aces_button.grid()
        self.zero_twos_button = Button(
            self._frame, text='Twos', command=self._zero_twos)
        self.zero_twos_button.grid()
        self.zero_threes_button = Button(
            self._frame, text='Threes', command=self._zero_threes)
        self.zero_threes_button.grid()
        self.zero_fours_button = Button(
            self._frame, text='Fours', command=self._zero_fours)
        self.zero_fours_button.grid()
        self.zero_fives_button = Button(
            self._frame, text='Fives', command=self._zero_fives)
        self.zero_fives_button.grid()
        self.zero_sixes_button = Button(
            self._frame, text='Sixes', command=self._zero_sixes)
        self.zero_sixes_button.grid()
        self.zero_three_same_button = Button(
            self._frame, text='3 of a kind', command=self._zero_three_same)
        self.zero_three_same_button.grid()
        self.zero_four_same_button = Button(
            self._frame, text='4 of a kind', command=self._zero_four_same)
        self.zero_four_same_button.grid()
        self.zero_full_house_button = Button(
            self._frame, text='Full House', command=self._zero_full_house)
        self.zero_full_house_button.grid()
        self.zero_small_straight_button = Button(
            self._frame, text='Small Straight', command=self._zero_small_straight)
        self.zero_small_straight_button.grid()
        self.zero_large_straight_button = Button(
            self._frame, text='Large Straight', command=self._zero_large_straight)
        self.zero_large_straight_button.grid()
        self.zero_chance_button = Button(
            self._frame, text='Chance', command=self._zero_chance)
        self.zero_chance_button.grid()
        self.zero_yatzy_button = Button(
            self._frame, text='Yatzy', command=self._zero_yatzy)
        self.zero_yatzy_button.grid()

    def _show_table(self):
        self.list.destroy()
        self.question.destroy()

        if self.aces_button != None:
            self.aces_button.destroy()
        if self.twos_button != None:
            self.twos_button.destroy()
        if self.threes_button != None:
            self.threes_button.destroy()
        if self.fours_button != None:
            self.fours_button.destroy()
        if self.fives_button != None:
            self.fives_button.destroy()
        if self.sixes_button != None:
            self.sixes_button.destroy()
        if self.three_same_button != None:
            self.three_same_button.destroy()
        if self.four_same_button != None:
            self.four_same_button.destroy()
        if self.full_house_button != None:
            self.full_house_button.destroy()
        if self.small_straight_button != None:
            self.small_straight_button.destroy()
        if self.large_straight_button != None:
            self.large_straight_button.destroy()
        if self.chance_button != None:
            self.chance_button.destroy()
        if self.yatzy_button != None:
            self.yatzy_button.destroy()
        if self.zero_aces_button != None:
            self.zero_aces_button.destroy()
        if self.zero_twos_button != None:
            self.zero_twos_button.destroy()
        if self.zero_threes_button != None:
            self.zero_threes_button.destroy()
        if self.zero_fours_button != None:
            self.zero_fours_button.destroy()
        if self.zero_fives_button != None:
            self.zero_fives_button.destroy()
        if self.zero_sixes_button != None:
            self.zero_sixes_button.destroy()
        if self.zero_three_same_button != None:
            self.zero_three_same_button.destroy()
        if self.zero_four_same_button != None:
            self.zero_four_same_button.destroy()
        if self.zero_full_house_button != None:
            self.zero_full_house_button.destroy()
        if self.zero_small_straight_button != None:
            self.zero_small_straight_button.destroy()
        if self.zero_large_straight_button != None:
            self.zero_large_straight_button.destroy()
        if self.zero_chance_button != None:
            self.zero_chance_button.destroy()
        if self.zero_yatzy_button != None:
            self.zero_yatzy_button.destroy()

        self.choose_zero_button.destroy()
        table = self.new_board.get_table()

        for score in table:
            self.board_list.insert(
                END, '{}: {}'.format(score, table[score]))
        self.board_list.grid()
        self.continue_button = Button(
            self._frame, text='Continue', command=self._roll_dice)
        self.continue_button.grid()

    def _zero_aces(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_aces(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have aces")
        else:
            self._show_table()

    def _zero_twos(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_twos(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have twos")
        else:
            self._show_table()

    def _zero_threes(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_threes(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have threes")
        else:
            self._show_table()

    def _zero_fours(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_fours(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have fours")
        else:
            self._show_table()

    def _zero_fives(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_fives(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have fives")
        else:
            self._show_table()

    def _zero_sixes(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_sixes(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have sixes")
        else:
            self._show_table()

    def _zero_three_same(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_three_same(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have three of a kind")
        else:
            self._show_table()

    def _zero_four_same(self):
        dice = [0, 0, 0, 0, 0]
        if self.new_board.mark_four_same(dice) == False:
            messagebox.showinfo("Choose something else",
                                "You already have four of a kind")
        else:
            self._show_table()

    def _zero_full_house(self):
        sum = 0
        if self.new_board.mark_full_house(sum) == False:
            messagebox.showinfo("Choose something else",
                                "You already have full house")
        else:
            self._show_table()

    def _zero_small_straight(self):
        num = 0
        if self.new_board.mark_small_straight(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have small straight")
        else:
            self._show_table()

    def _zero_large_straight(self):
        num = 0
        if self.new_board.mark_large_straight(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have large straight")
        else:
            self._show_table()

    def _zero_chance(self):
        sum = 0
        if self.new_board.mark_chance(sum) == False:
            messagebox.showinfo("Choose something else",
                                "You already have chance")
        else:
            self._show_table()

    def _zero_yatzy(self):
        num = 0
        if self.new_board.mark_yatzy(num) == False:
            messagebox.showinfo("Choose something else",
                                "You already have yatzy")
        else:
            self._show_table()
