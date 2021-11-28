from tkinter import *
from tkinter import ttk, constants
from services.dice import Dice
from services.player_service import PlayerService


class PlayView:
    def __init__(self, root):
        self._root = root
        self._dice = [1, 1, 1, 1, 1]
        self.add_button = None
        self.frame = None
        self._initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def clear_frame(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()

    def roll_dice(self):
        self.frame.forget()
        rolling_dice = Dice(self._root)
        rolling_dice.roll_dice(self._dice)

    def _initialize(self):
        self.frame = Frame(master=self._root)
        self.add_button = ttk.Button(
            self.frame, text='ROLL DICE', command=self.roll_dice).grid()
        table = ttk.Treeview(self.frame)
        table['columns'] = ('Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Bonus', '3 of a kind',
                            '4 of a kind', 'Full House', 'Small Straight', 'Large Straight', 'Chance', 'Yatzy', 'Total')

        table.column("#0", width=0,  stretch=NO)
        table.column("Aces", anchor=CENTER, width=50)
        table.heading("Aces", text="Aces")
        table.column("Twos", anchor=CENTER, width=50)
        table.heading("Twos", text="Twos")
        table.column("Threes", anchor=CENTER, width=55)
        table.heading("Threes", text="Threes")
        table.column("Fours", anchor=CENTER, width=50)
        table.heading("Fours", text="Fours")
        table.column("Fives", anchor=CENTER, width=50)
        table.heading("Fives", text="Fives")
        table.column("Sixes", anchor=CENTER, width=50)
        table.heading("Sixes", text="Sixes")
        table.column("Bonus", anchor=CENTER, width=50)
        table.heading("Bonus", text="Bonus")
        table.column("3 of a kind", anchor=CENTER, width=90)
        table.heading("3 of a kind", text="3 of a kind")
        table.column("4 of a kind", anchor=CENTER, width=90)
        table.heading("4 of a kind", text="4 of a kind")
        table.column("Full House", anchor=CENTER, width=85)
        table.heading("Full House", text="Full House")
        table.column("Small Straight", anchor=CENTER, width=120)
        table.heading("Small Straight", text="Small Straight")
        table.column("Large Straight", anchor=CENTER, width=120)
        table.heading("Large Straight", text="Large Straight")
        table.column("Chance", anchor=CENTER, width=60)
        table.heading("Chance", text="Chance")
        table.column("Yatzy", anchor=CENTER, width=50)
        table.heading("Yatzy", text="Yatzy")
        table.column("Total", anchor=CENTER, width=50)
        table.heading("Total", text="Total")
        table.grid()
