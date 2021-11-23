from tkinter import *
from tkinter import ttk, constants
from services.dice import Dice

class PlayView:
    def __init__(self, root):
        self._root = root
        self._dice = [1,1,1,1,1]
        self._frame = None
        self._roll = None
        self._add_button = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def roll_dice(self):
        self._add_button.destroy()
        self._roll = ttk.Label(self._root, text="Choose which dice you want to roll again:").pack()
        rolling_dice = Dice(self._root)
        rolling_dice.roll_dice(self._dice)
            
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._add_button = ttk.Button(master=self._frame, text='ROLL DICE', command=self.roll_dice)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        self._add_button.grid(padx=5, pady=5, sticky=constants.EW)
