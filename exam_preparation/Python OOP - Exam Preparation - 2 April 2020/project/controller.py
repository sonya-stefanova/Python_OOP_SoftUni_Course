from project.battle_field import BattleField
from project.core.card_factory import CardFactory
from project.core.player_factory import PlayerFactory
from project.player import player
from project.player.player_repository import PlayerRepository
from project.card.card_repository import CardRepository


class Controller:

    def __init__(self):
        self.player_repository = PlayerRepository()
        self.card_repository = CardRepository()

        self.player_factory = PlayerFactory()
        self.card_factory = CardFactory()

    def add_player(self, type, username):
        """Creates a player with the provided type and name. The method should return the following message:
"Successfully added player of type {type} with username: {username}"
"""
        player = self.player_factory.create_player(type, username)
        if not player:
            return
        self.player_repository.add(player)
        return f"Successfully added player of type {type} with username: {username}"

    def add_card(self, type, name):
        """Creates a card with the provided type -> "Magic" or "Trap" and name.
        The method should return the following message:
        "Successfully added card of type {type}Card with name: {name}"
"""
        card = self.card_factory.create_card(type, name)
        if not card:
            return
        self.card_repository.add(card)
        return f"Successfully added card of type {type}Card with name: {name}"

    def add_player_card(self, username, card_name):
        """Adds the given card to the user card repository.
        The method should return the following message:
        "Successfully added card: {card_name} to user: {username}"
"""
        card = self.card_repository.find(card_name)
        player = self.player_repository.find(username)
        player.card_repository.add(card)
        return f"Successfully added card: {card_name} to user: {username}"

    def fight(self, attack_name, enemy_name):
        """The attacker and the enemy start a fight in a battlefield. The method should return the following message:
        "Attack user health {attacker_health_left} - Enemy user health {enemy_health_left}"
        """
        attacker = self.player_repository.find(attack_name)
        enemy = self.player_repository.find(enemy_name)

        battle_field = BattleField()

        battle_field.fight(attacker, enemy)
        return f"Attack user health {attacker.health} - Enemy user health {enemy.health}"


    def report(self):
        """Returns a report message in format:
    Username: {username1} - Health: {health1} - Cards {cards_count1}
    ### Card: {name1} - Damage: {card_damage1}
    …
"""
        result = ""
        for p in self.player_repository.players:
            result +=str(p) + "\n"
        for c in self.card_repository.cards:
            result+=str(c)+"\n"
        return result.strip()
