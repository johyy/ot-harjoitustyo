from ui.index_view import IndexView
from ui.play_view import PlayView
from ui.players_view import PlayersView
from ui.choose_player import ChoosePlayerView
from ui.board_view import BoardView
from ui.dice_view import DiceView


class UI:
    def __init__(self, root):
        self.root = root
        self._current_view = None

    def start(self):
        self.show_index_view()

    def hide_current_view(self):
        if self._current_view:
            self._current_view = None

    def _handle_play_view(self, playername):
        self.show_play_view(playername)

    def _handle_players_view(self):
        self.show_players_view()

    def _handle_choose_player_view(self):
        self.show_choose_player_view()

    def _handle_board_view(self, playername, dice, sum):
        self.show_board_view(playername, dice, sum)

    def _handle_dice_view(self, playername):
        self.show_dice_view(playername)

    def _handle_index_view(self):
        self.show_index_view()

    def show_dice_view(self, playername):
        self.hide_current_view()
        self._current_view = DiceView(
            self.root, playername, self._handle_board_view)

    def show_board_view(self, playername, dice, sum):
        self.hide_current_view()
        self._current_view = BoardView(
            self.root, playername, dice, sum, self._handle_play_view, self._handle_index_view)

    def show_index_view(self):
        self.hide_current_view()
        self._current_view = IndexView(
            self.root, self._handle_choose_player_view, self._handle_players_view)

    def show_play_view(self, playername):
        self.hide_current_view()
        self._current_view = PlayView(
            self.root, playername, self._handle_dice_view)

    def show_players_view(self):
        self.hide_current_view()
        self._current_view = PlayersView(
            self.root, self._handle_choose_player_view)

    def show_choose_player_view(self):
        self.hide_current_view()
        self._current_view = ChoosePlayerView(
            self.root, self._handle_play_view, self._handle_players_view)
