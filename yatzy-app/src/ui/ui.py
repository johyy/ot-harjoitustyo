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
        self.table = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Bonus": 0, "Three of a kind": 0,
                      "Four of a kind": 0, "Full house": 0, "Small straight": 0, "Large straight": 0, "Chance": 0, "Yatzy": 0}

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

    def _handle_board_view(self, dice, sum):
        self.show_board_view(dice, sum)

    def _handle_dice_view(self):
        self.show_dice_view()

    def show_dice_view(self):
        self.hide_current_view()
        self._current_view = DiceView(self.root, self._handle_board_view)

    def show_board_view(self, dice, sum):
        self.hide_current_view()
        self._current_view = BoardView(
            self.root, dice, sum, self._handle_play_view)

    def show_index_view(self):
        self.hide_current_view()
        self._current_view = IndexView(
            self.root, self._handle_choose_player_view, self._handle_players_view)

    def show_play_view(self):
        self.hide_current_view()
        self._current_view = PlayView(self.root, self._handle_dice_view)

    def show_players_view(self):
        self.hide_current_view()
        self._current_view = PlayersView(self.root, self._handle_play_view)

    def show_choose_player_view(self):
        self.hide_current_view()
        self._current_view = ChoosePlayerView(
            self.root, self._handle_play_view)
