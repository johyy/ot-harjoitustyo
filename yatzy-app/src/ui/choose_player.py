from tkinter import ttk, constants, messagebox
from services.player_service import player_service


class ChoosePlayerView:
    def __init__(self, root, handle_play_view, handle_players_view):
        self._root = root
        self._handle_play_view = handle_play_view
        self._handle_players_view = handle_players_view
        self._frame = None
        self.list = player_service.get_all_players()
        self.player = None
        self.box = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def playbutton(self):
        self.player = self.box.get()
        if self.player:
            messagebox.showinfo('You choose the name ', self.player)
            self._frame.destroy()
            self._handle_play_view(self.player)
        else:
            messagebox.showinfo('Stop right now!',
                                'You have to choose a player name')

    def playersbutton(self):
        self._frame.destroy()
        self._handle_players_view()

    def names_in_box(self):
        self.box = ttk.Combobox(self._frame, values=self.list)
        self.box.grid()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._frame.grid()
        label = ttk.Label(
            self._frame, text="Choose yourself a playername. You can also add a new player!")
        label.grid()
        self.names_in_box()
        players_button = ttk.Button(
            master=self._frame, text='Add a new player', command=self.playersbutton)
        play_button = ttk.Button(
            master=self._frame, text='Play!', command=self.playbutton)

        self._frame.grid_columnconfigure(0, weight=1, minsize=400)
        play_button.grid()
        players_button.grid()
