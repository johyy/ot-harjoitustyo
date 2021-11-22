from tkinter import *
from tkinter import ttk, constants
from random import randint


class PlayView:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self.dice = [1,1,1,1,1]
        self.text = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def roll_dice(self):
        if self.text != None:
            self.text.destroy()
        new_dice = []
        for die in self.dice:
            die = randint(1, 6)
            new_dice.append(die)
        self.show_dice(new_dice)

    def show_dice(self, list_of_dice):
        self.text = Text(self._root)
        
        for die in list_of_dice:
            self.text.insert(END, str(die) + '\n')
        self.text.pack()
            

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        add_button = ttk.Button(master=self._frame, text='Roll dice', command=self.roll_dice)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        add_button.grid(padx=5, pady=5, sticky=constants.EW)
