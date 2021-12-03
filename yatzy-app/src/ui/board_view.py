from tkinter import *
from services.board import Board

class BoardView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.new_board = Board()

    def select(self, sum, dice):
        self._frame = Frame(master=self._root)
        self._frame.grid()
        question = Label(
            self._frame, text="How do you want to use these " + str(sum) + " points?")

        list = Listbox(self._frame)
        i = 0
        while i < len(dice):
            list.insert(i, str(dice[i]))
            i += 1
        list.grid()
        question.grid()

        if self.new_board.check_aces(dice):
            aces = Button(
                self._frame, text='Aces', command=self.new_board.aces).grid()
        if self.new_board.check_twos(dice):
            twos = Button(
                self._frame, text='Twos', command=self.new_board.twos).grid()
        if self.new_board.check_threes(dice):
            threes = Button(
                self._frame, text='Threes', command=self.new_board.threes).grid()
        if self.new_board.check_fours(dice):
            fours = Button(
                self._frame, text='Fours', command=self.new_board.fours).grid()
        if self.new_board.check_fives(dice):
            fives = Button(
                self._frame, text='Fives', command=self.new_board.fives).grid()
        if self.new_board.check_sixes(dice):
            sixes = Button(
                self._frame, text='Sixes', command=self.new_board.sixes).grid()
        if self.new_board.check_three_kind(dice):
            three_same = Button(
                self._frame, text='3 of a kind', command=self.new_board.three_same).grid()
        if self.new_board.check_four_kind(dice):
            four_same = Button(
                self._frame, text='4 of a kind', command=self.new_board.four_same).grid()
        if  self.new_board.check_full_house(dice):
            full_house = Button(
                self._frame, text='Full House', command=self.new_board.full_house).grid()
        if self.new_board.check_small_straight(dice):
            small_straight = Button(
                self._frame, text='Small Straight', command=self.new_board.small_straight).grid()
        if self.new_board.check_large_straight(dice):
            large_straight = Button(
                self._frame, text='Large Straight', command=self.new_board.large_straight).grid()
        chance = Button(
            self._frame, text='Chance', command=self.new_board.chance).grid()
        if self.new_board.check_yatzy(dice):
            yatzy = Button(
                self._frame, text='Yatzy', command=self.new_board.yatzy).grid()