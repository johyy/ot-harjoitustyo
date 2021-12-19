from tkinter import *
from tkinter import ttk, constants, messagebox
from services.player_service import player_service


class PlayersView:
    def __init__(self, root, handle_choose_player_view):
        self._root = root
        self._handle_choose_player_view = handle_choose_player_view
        self._frame = None
        self._player_entry = None

        self._initialize()

    def choose_player_button(self):
        self._frame.destroy()
        self._handle_choose_player_view()

    def _initialize_player_field(self):
        player_label = ttk.Label(
            master=self._frame, text='Come up with a player name for yourself...')
        self._player_entry = ttk.Entry(self._frame)

        player_label.grid(padx=5, pady=5, sticky=constants.W)
        self._player_entry.grid(padx=5, pady=5, sticky=constants.EW)

    def add_player(self):
        new_player = self._player_entry.get()

        if len(new_player) > 0 and len(new_player) < 21:

            player_service.create_player(new_player)
            messagebox.showinfo(new_player, 'Added to the players!')

        else:
            messagebox.showerror(
                'Error', 'The length of the player name should be between 0 and 20')

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid()

        self._initialize_player_field()

        add_button = ttk.Button(
            master=self._frame, text='Add a player', command=self.add_player)
        add_button.grid()
        player_button = ttk.Button(
            master=self._frame, text='Return', command=self.choose_player_button)
        player_button.grid()
