from tkinter import ttk, messagebox
from tkinter import *


class IndexView:
    def __init__(self, root, handle_play_view, handle_players_view):
        self._root = root
        self._handle_play_view = handle_play_view
        self._handle_players_view = handle_players_view

        self._root["bg"] = "black"
        self.canvas = Canvas(self._root, width=1000, height=6000)
        self.canvas["bg"] = "black"
        self.canvas.pack()
        self._initialize()

    def yatzybutton(self):
        messagebox.showinfo('Yatzyyy', 'Are you ready to play?')

    def playbutton(self):
        self.canvas.destroy()
        self._handle_play_view()

    def playersbutton(self):
        self.canvas.destroy()
        self._handle_players_view()

    def _initialize(self):

        yatzypic = PhotoImage(file="src/pictures/yatzypic.png")
        play = PhotoImage(file="src/pictures/play.png")
        players = PhotoImage(file="src/pictures/players.png")

        yatzy_button = ttk.Button(
            self.canvas, image=yatzypic, command=self.yatzybutton).grid(row=1, column=2)
        play_button = ttk.Button(
            self.canvas, image=play, command=self.playbutton).grid(row=2, column=2)
        players_button = ttk.Button(
            self.canvas, image=players, command=self.playersbutton).grid(row=3, column=2)

        self._root.mainloop()
