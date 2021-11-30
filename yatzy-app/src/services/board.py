import tkinter as tk
from tkinter import Listbox, ttk


class Board:
    def __init__(self, root):
        self._root = root
        self._frame = None

    def select(self, sum, dice):
        self._frame = tk.Frame(master=self._root)
        self._frame.grid()
        question = tk.Label(
            self._frame, text="How do you want to use these " + str(sum) + " points?")

        list = tk.Listbox(self._frame)
        i = 0
        while i < len(dice):
            list.insert(i, str(dice[i]))
            i += 1
        list.grid()
        question.grid()

        if 1 in dice:
            aces = ttk.Button(
                self._frame, text='Aces', command=self.aces).grid()
        if 2 in dice:
            twos = ttk.Button(
                self._frame, text='Twos', command=self.twos).grid()
        if 3 in dice:
            threes = ttk.Button(
                self._frame, text='Threes', command=self.threes).grid()
        if 4 in dice:
            fours = ttk.Button(
                self._frame, text='Fours', command=self.fours).grid()
        if 5 in dice:
            fives = ttk.Button(
                self._frame, text='Fives', command=self.fives).grid()
        if 6 in dice:
            sixes = ttk.Button(
                self._frame, text='Sixes', command=self.sixes).grid()
        three_same = ttk.Button(
            self._frame, text='3 of a kind', command=self.three_same).grid()
        four_same = ttk.Button(
            self._frame, text='4 of a kind', command=self.four_same).grid()
        full_house = ttk.Button(
            self._frame, text='Full House', command=self.full_house).grid()
        small_straight = ttk.Button(
            self._frame, text='Small Straight', command=self.small_straight).grid()
        large_straight = ttk.Button(
            self._frame, text='Large Straight', command=self.large_straight).grid()
        chance = ttk.Button(
            self._frame, text='Chance', command=self.chance).grid()
        yatzy = ttk.Button(
            self._frame, text='Yatzy', command=self.yatzy).grid()

    def aces(self):
        pass

    def twos(self):
        pass

    def threes(self):
        pass

    def fours(self):
        pass

    def fives(self):
        pass

    def sixes(self):
        pass

    def three_same(self):
        pass

    def four_same(self):
        pass

    def full_house(self):
        pass

    def small_straight(self):
        pass

    def large_straight(self):
        pass

    def chance(self):
        pass

    def yatzy(self):
        pass
