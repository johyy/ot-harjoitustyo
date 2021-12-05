from tkinter import *
from services.dice import Dice


class DiceView:
    def __init__(self, root, handle_board_view):
        self._root = root
        self.handle_board_view = handle_board_view
        self.new_dice = Dice()
        self.round = 1
        self.dice = [1, 1, 1, 1, 1]

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
        self.first_dice = []
        self.second_dice = []
        self.selected_dice = []
        self.new_roll_dice = []
        self.selected_dice2 = []
        self.new_roll_dice2 = []

        self.vars = []
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.vars.append(self.var1)
        self.vars.append(self.var2)
        self.vars.append(self.var3)
        self.vars.append(self.var4)
        self.vars.append(self.var5)

        self.vars2 = []
        self.var1_2 = IntVar()
        self.var2_2 = IntVar()
        self.var3_2 = IntVar()
        self.var4_2 = IntVar()
        self.var5_2 = IntVar()
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

        self._initialize()

    def _initialize(self):
        if self._frame == None:
            self._frame = Frame(master=self._root)
            self._frame.grid()
        if self.round == 1:
            self.show_dice(self.new_dice.roll_dice(self.dice))
        elif self.round == 2:
            self.mix_dice(self.new_dice.roll_dice(self.new_roll_dice))

    def roll_again(self):
        self.roll_again_button.destroy()
        self._initialize()

    def mix_dice(self, rolled_dice):
        self.show_second_dice(self.new_dice.mix_dice(
            rolled_dice, self.selected_dice))

    def show_dice(self, dice):
        self._roll = Label(
            self._frame, text="Choose which dice you want to hold")
        self._roll.grid()

        self._check1 = Checkbutton(
            self._frame, text=dice[0], variable=self.vars[0])
        self._check1.grid()
        self.first_dice.append(dice[0])

        self._check2 = Checkbutton(
            self._frame, text=dice[1], variable=self.vars[1])
        self._check2.grid()
        self.first_dice.append(dice[1])

        self._check3 = Checkbutton(
            self._frame, text=dice[2], variable=self.vars[2])
        self._check3.grid()
        self.first_dice.append(dice[2])

        self._check4 = Checkbutton(
            self._frame, text=dice[3], variable=self.vars[3])
        self._check4.grid()
        self.first_dice.append(dice[3])

        self._check5 = Checkbutton(
            self._frame, text=dice[4], variable=self.vars[4])
        self._check5.grid()
        self.first_dice.append(dice[4])

        self.choose_button = Button(
            self._frame, text='I have chosen!', command=self.var_states)
        self.choose_button.grid()

    def show_second_dice(self, dice):
        if self._roll != None:
            self._roll.destroy()
        elif self.choose_button != None:
            self.choose_button.destroy()

        self._second_roll = Label(
            self._frame, text="Now choose which dice you want to use")
        self._second_roll.grid()

        self._check21 = Checkbutton(
            self._frame, text=dice[0], variable=self.vars2[0])
        self._check21.grid()
        self.second_dice.append(dice[0])

        self._check22 = Checkbutton(
            self._frame, text=dice[1], variable=self.vars2[1])
        self._check22.grid()
        self.second_dice.append(dice[1])

        self._check23 = Checkbutton(
            self._frame, text=dice[2], variable=self.vars2[2])
        self._check23.grid()
        self.second_dice.append(dice[2])

        self._check24 = Checkbutton(
            self._frame, text=dice[3], variable=self.vars2[3])
        self._check24.grid()
        self.second_dice.append(dice[3])

        self._check25 = Checkbutton(
            self._frame, text=dice[4], variable=self.vars2[4])
        self._check25.grid()
        self.second_dice.append(dice[4])

        self._second_choose_button = Button(
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
        self.roll_again_button = Button(
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
        self.dice_total_button = Button(
            self._frame, text='Continue', command=self.go_to_board)
        self.dice_total_button.grid()

    def go_to_board(self):
        self._frame.destroy()
        self.dice_total_button.destroy()
        new_sum = self.new_dice.dice_total(self.selected_dice2)
        self.handle_board_view(self.selected_dice2, new_sum)
