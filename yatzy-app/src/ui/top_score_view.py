from tkinter import ttk
from tkinter import *
from services.player_service import player_service


class TopScoreView:
    def __init__(self, root, handle_choose_player_view):
        self._root = root
        self.handle_choose_player_view = handle_choose_player_view
        self.frame = None
        self.list = None
        self._initialize()

    def _initialize(self):
        i = 1
        self.frame = Frame(master=self._root)
        self.frame.grid()
        playerlist = player_service.get_all_players_and_points()
        Label(self.frame, text="Top Score", font=(
            "Arial", 30)).grid(row=0, columnspan=3)

        cols = ('Name', 'Score')
        listBox = ttk.Treeview(self.frame, columns=cols, show='headings')

        for col in cols:
            listBox.heading(col, text=col)
            listBox.grid(row=1, column=0, columnspan=2)

        while i < len(playerlist):
            listBox.insert("", "end", values=(playerlist[i-1], playerlist[i]))
            i += 2

        self.get_back_button = Button(
            self.frame, text='Play!', command=self._play)
        self.get_back_button.grid()

    def _play(self):
        self.frame.destroy()
        self.handle_choose_player_view()
