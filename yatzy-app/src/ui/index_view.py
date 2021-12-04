from tkinter import ttk, messagebox
from tkinter import *


class IndexView:
    def __init__(self, root, handle_choose_player_view, handle_players_view):
        self._root = root
        self._handle_choose_player_view = handle_choose_player_view
        self._handle_players_view = handle_players_view

        self._root["bg"] = "black"
        self._frame = None
        self._initialize()

    def yatzybutton(self):
        messagebox.showinfo('Yatzyyy', 'Are you ready to play?')

    def playbutton(self):
        self._frame.destroy()
        self._handle_choose_player_view()

    def playersbutton(self):
        self._frame.destroy()
        self._handle_players_view()

    def _initialize(self):

        self._frame = Frame(master=self._root, background='Black')
        self._frame.grid()

        yatzypic = PhotoImage(file="src/pictures/yatzypic.png")
        play = PhotoImage(file="src/pictures/play.png")
        players = PhotoImage(file="src/pictures/players.png")

        yatzy_button = ttk.Button(
            self._frame, image=yatzypic, command=self.yatzybutton)
        yatzy_button.grid(row=1, column=2)
        play_button = ttk.Button(
            self._frame, image=play, command=self.playbutton)
        play_button.grid(row=2, column=2)
        players_button = ttk.Button(
            self._frame, image=players, command=self.playersbutton)
        players_button.grid(row=3, column=2)

        self._root.mainloop()
