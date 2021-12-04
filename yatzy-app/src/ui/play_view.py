from tkinter import *

class PlayView:
    def __init__(self, root, handle_dice_view):
        self._root = root
        self.handle_dice_view = handle_dice_view
        self.table = None
        self.add_button = None
        self.frame = None
        self._initialize()

    def roll_dice(self):
        self.frame.destroy()
        self.handle_dice_view()

    def _initialize(self):
        self.frame = Frame(master=self._root)
        self.frame.grid()
        self.add_button = Button(
            self.frame, text='ROLL DICE', command=self.roll_dice)
        self.add_button.grid()