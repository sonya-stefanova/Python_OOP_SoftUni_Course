from project.player.player import Player


class BattleField:
    """That's the most interesting method.
•	If one of the users is_dead, raise new ValueError with message "Player is dead!"
•	If a player is a beginner, increase his health with 40 points and increase the damage points of each card in the players' deck with 30.
•	Before the fight, both players get bonus health points from their deck. (sum of all health points of his cards)
•	Attacker attacks first and after that the enemy attacks (deal damage points to opponent for each card). If one of the players is dead, you should stop the fight.
"""

    def fight(self, attacker, enemy):
        if attacker.is_dead or enemy.is_dead:
            raise ValueError("Player is dead!")

        if attacker.__class__.__name__ == "Beginner":
            self.increase_beginner(attacker)

        self.get_bonus_points(attacker)
        self.get_bonus_points(enemy)

        for card in attacker.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            enemy.take_damage(card.damage_points)

        for card in enemy.card_repository.cards:
            if enemy.is_dead or attacker.is_dead:
                return
            attacker.take_damage(card.damage_points)

    @staticmethod
    def increase_beginner(player):
        player.health += 40
        for card in player.card_repository.cards:
            card.damage_points += 30

    @staticmethod
    def get_bonus_points(player):
        player.health += sum([card.health_points for card in player.card_repository.cards])