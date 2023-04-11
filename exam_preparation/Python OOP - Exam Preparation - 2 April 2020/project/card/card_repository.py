from project.card.card import Card


class CardRepository:

    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        """Adds a card in the collection.
        •	If a card exists with a name equal to the name of the given card,
        raise a ValueError with message "Card {name} already exists!".
        •	Otherwise, add the card and increase the count
"""
        if card.name in [c.name for c in self.cards]:
            raise ValueError(f"Card {card.name} already exists!")
        self.cards.append(card)
        self.count += 1

    def remove(self, card:str):
        """Removes a card from the collection
    •	If the card is an empty string, raise a ValueError with message "Card cannot be an empty string!".
    •	Otherwise, remove the card and decrease the count
"""
        if not card:
            raise ValueError("Card cannot be an empty string!")
        self.cards.remove(card)
        self.count-=1

    def find(self, name: str):
        for card in self.cards:
            if card.name == name:
                return card
        #next(filter(lambda c: c.name == name, self.cards), None)
        #[c for c in self.cards if c.name == name][0]