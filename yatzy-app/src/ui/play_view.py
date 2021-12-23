from tkinter import *


class PlayView:
    def __init__(self, root, playername, handle_dice_view):
        self._root = root
        self.handle_dice_view = handle_dice_view
        self.playername = playername
        self.table = None
        self.add_button = None
        self.frame = None
        self._initialize()

    def _roll_dice(self):
        self.frame.destroy()
        self.handle_dice_view(self.playername)

    def _initialize(self):
        self._root.title(self.playername + ' plays yatzy')
        self.frame = Frame(master=self._root)
        self.frame.grid()
        self.add_button = Button(
            self.frame, text='ROLL DICE', command=self._roll_dice)
        self.add_button.grid()
