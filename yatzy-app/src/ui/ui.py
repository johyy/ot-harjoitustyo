from ui.index_view import IndexView
from ui.play_view import PlayView
from ui.players_view import PlayersView
from ui.choose_player import ChoosePlayerView


class UI:
    def __init__(self, root):
        self.root = root
        self._current_view = None

    def start(self):
        self.show_index_view()

    def hide_current_view(self):
        if self._current_view:
            self._current_view = None

    def _handle_play_view(self):
        self.show_play_view()

    def _handle_players_view(self):
        self.show_players_view()

    def _handle_choose_player_view(self):
        self.show_choose_player_view()

    def show_index_view(self):
        self.hide_current_view()
        self._current_view = IndexView(
            self.root, self._handle_choose_player_view, self._handle_players_view)

    def show_play_view(self):
        self.hide_current_view()
        self._current_view = PlayView(self.root)
        self._current_view.pack()

    def show_players_view(self):
        self.hide_current_view()
        self._current_view = PlayersView(self.root, self._handle_play_view)

        self._current_view.pack()

    def show_choose_player_view(self):
        self.hide_current_view()
        self._current_view = ChoosePlayerView(
            self.root, self._handle_play_view)

        self._current_view.pack()
