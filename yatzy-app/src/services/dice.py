import tkinter as tk
from tkinter import ttk
from random import randint
from services.board import Board


class Dice:
    def __init__(self, root):
        self._root = root
        self._check = None
        self._final_check = None
        self.choose_button = None
        self._second_choose_button = None
        self.roll_again_button = None
        self._frame = None
        self._roll = None
        self._second_roll = None
        self.dice_total_button = None
        self.continue_button = None
        self.mixed_dice = []
        self.sum = 0
        self.first_dice = []
        self.second_dice = []
        self.new_dice = []
        self.round = 1
        self.selected_dice = []
        self.new_roll_dice = []
        self.selected_dice2 = []
        self.new_roll_dice2 = []

        self.vars = []
        self.var1 = tk.IntVar()
        self.var2 = tk.IntVar()
        self.var3 = tk.IntVar()
        self.var4 = tk.IntVar()
        self.var5 = tk.IntVar()
        self.vars.append(self.var1)
        self.vars.append(self.var2)
        self.vars.append(self.var3)
        self.vars.append(self.var4)
        self.vars.append(self.var5)

        self.vars2 = []
        self.var1_2 = tk.IntVar()
        self.var2_2 = tk.IntVar()
        self.var3_2 = tk.IntVar()
        self.var4_2 = tk.IntVar()
        self.var5_2 = tk.IntVar()
        self.vars2.append(self.var1_2)
        self.vars2.append(self.var2_2)
        self.vars2.append(self.var3_2)
        self.vars2.append(self.var4_2)
        self.vars2.append(self.var5_2)

        self._check1 = None
        self._check2 = None
        self._check3 = None
        self._check4 = None
        self._check5 = None

        self._check21 = None
        self._check22 = None
        self._check23 = None
        self._check24 = None
        self._check25 = None

    def roll_dice(self, dice):
        self._frame = tk.Frame(master=self._root)
        self._frame.grid()
        self.new_dice.clear()
        for die in dice:
            die = randint(1, 6)
            self.new_dice.append(die)
        if self.round == 1:
            self.show_dice(self.new_dice)
        elif self.round == 2:
            self.mix_dice(self.new_dice)

    def roll_again(self):
        self.roll_again_button.destroy()
        self.roll_dice(self.new_roll_dice)

    def show_dice(self, dice):
        self._roll = tk.Label(
            self._frame, text="Choose which dice you want to hold")
        self._roll.grid()

        self._check1 = ttk.Checkbutton(
            self._frame, text=dice[0], variable=self.vars[0])
        self._check1.grid()
        self.first_dice.append(dice[0])

        self._check2 = ttk.Checkbutton(
            self._frame, text=dice[1], variable=self.vars[1])
        self._check2.grid()
        self.first_dice.append(dice[1])

        self._check3 = ttk.Checkbutton(
            self._frame, text=dice[2], variable=self.vars[2])
        self._check3.grid()
        self.first_dice.append(dice[2])

        self._check4 = ttk.Checkbutton(
            self._frame, text=dice[3], variable=self.vars[3])
        self._check4.grid()
        self.first_dice.append(dice[3])

        self._check5 = ttk.Checkbutton(
            self._frame, text=dice[4], variable=self.vars[4])
        self._check5.grid()
        self.first_dice.append(dice[4])

        self.choose_button = ttk.Button(
            self._frame, text='I have chosen!', command=self.var_states)
        self.choose_button.grid()

    def show_second_dice(self, dice):
        if self._roll is not None:
            self._roll.destroy()
        elif self.choose_button is not None:
            self.choose_button.destroy

        self._second_roll = tk.Label(
            self._frame, text="Now choose which dice you want to use")
        self._second_roll.grid()

        self._check21 = ttk.Checkbutton(
            self._frame, text=dice[0], variable=self.vars2[0])
        self._check21.grid()
        self.second_dice.append(dice[0])

        self._check22 = ttk.Checkbutton(
            self._frame, text=dice[1], variable=self.vars2[1])
        self._check22.grid()
        self.second_dice.append(dice[1])

        self._check23 = ttk.Checkbutton(
            self._frame, text=dice[2], variable=self.vars2[2])
        self._check23.grid()
        self.second_dice.append(dice[2])

        self._check24 = ttk.Checkbutton(
            self._frame, text=dice[3], variable=self.vars2[3])
        self._check24.grid()
        self.second_dice.append(dice[3])

        self._check25 = ttk.Checkbutton(
            self._frame, text=dice[4], variable=self.vars2[4])
        self._check25.grid()
        self.second_dice.append(dice[4])

        self._second_choose_button = ttk.Button(
            self._frame, text='Ready!', command=self.var_states_two)
        self._second_choose_button.grid()

    def var_states(self):
        if self.var1.get() != 0:
            self.selected_dice.append(self.first_dice[0])
        else:
            self.new_roll_dice.append(self.first_dice[0])

        if self.var2.get() != 0:
            self.selected_dice.append(self.first_dice[1])
        else:
            self.new_roll_dice.append(self.first_dice[1])

        if self.var3.get() != 0:
            self.selected_dice.append(self.first_dice[2])
        else:
            self.new_roll_dice.append(self.first_dice[2])

        if self.var4.get() != 0:
            self.selected_dice.append(self.first_dice[3])
        else:
            self.new_roll_dice.append(self.first_dice[3])

        if self.var5.get() != 0:
            self.selected_dice.append(self.first_dice[4])
        else:
            self.new_roll_dice.append(self.first_dice[4])

        self.round += 1
        self.choose_button.destroy()
        self._check1.destroy()
        self._check2.destroy()
        self._check3.destroy()
        self._check4.destroy()
        self._check5.destroy()
        self.roll_again_button = ttk.Button(
            self._frame, text='Roll again', command=self.roll_again)
        self.roll_again_button.grid()

    def var_states_two(self):
        if self.var1_2.get() != 0:
            self.selected_dice2.append(self.second_dice[0])

        if self.var2_2.get() != 0:
            self.selected_dice2.append(self.second_dice[1])

        if self.var3_2.get() != 0:
            self.selected_dice2.append(self.second_dice[2])

        if self.var4_2.get() != 0:
            self.selected_dice2.append(self.second_dice[3])

        if self.var5_2.get() != 0:
            self.selected_dice2.append(self.second_dice[4])

        self._second_choose_button.destroy()
        self._second_roll.destroy()
        self._check21.destroy()
        self._check22.destroy()
        self._check23.destroy()
        self._check24.destroy()
        self._check25.destroy()
        self.dice_total_button = ttk.Button(
            self._frame, text='See the total', command=self.dice_total)
        self.dice_total_button.grid()

    def mix_dice(self, rolled_dice):
        self.mixed_dice = []
        for die1 in rolled_dice:
            self.mixed_dice.append(die1)
        if len(self.selected_dice) > 0:
            for die2 in self.selected_dice:
                self.mixed_dice.append(die2)

        self.show_second_dice(self.mixed_dice)

    def dice_total(self):
        self.dice_total_button.destroy()
        i = 0
        while i < len(self.selected_dice2):
            self.sum += self.selected_dice2[i]
            i += 1
        total = tk.Label(
            self._frame, text="Your total sum of dice is " + str(self.sum))
        total.grid()
        self.continue_button = ttk.Button(
            self._frame, text='Continue', command=self.go_to_board).grid()

    def go_to_board(self):
        self._frame.destroy()
        board = Board(self._root)
        board.select(self.sum, self.selected_dice2)
