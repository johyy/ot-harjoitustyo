from tkinter import *
from tkinter import ttk, constants
from services.player_service import player_service


class ChoosePlayerView:
    def __init__(self, root, handle_play_view):
        self._root = root
        self._handle_play_view = handle_play_view
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def playbutton(self):
        self._frame.destroy()
        self._handle_play_view()

    def playernames(self):
        pass

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid()
        play_button = ttk.Button(
            master=self._frame, text='Play!', command=self.playbutton)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        play_button.grid()
