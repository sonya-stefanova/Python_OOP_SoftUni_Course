from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class CardFactory:
    VALID_CARDS_TYPES = {
        "Magic": MagicCard,
        "Trap": TrapCard
    }

    def create_card(self,type, name):
        if type in self.VALID_CARDS_TYPES:
            return self.VALID_CARDS_TYPES[type](name)