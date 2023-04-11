from project.player.advanced import Advanced
from project.player.beginner import Beginner


class PlayerFactory:

    VALID_PLAYERS = {
        "Beginner": Beginner,
        "Advanced": Advanced
    }

    def create_player(self, type, username):
        if type not in self.VALID_PLAYERS:
            return None
        return self.VALID_PLAYERS[type](username)