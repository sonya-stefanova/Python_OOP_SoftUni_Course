from project.player import Player


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def _find_player(self, player_name):
        for player in self.players:
            if player.name == player_name:
                return player

    def _get_supply_by_type(self, supply_type):
        for idx in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[idx]
            if supply.__class__.__name__ == supply_type:
                return idx, supply
        return -1, None

    def add_player(self, *args):
        added = []
        for player in args:
            if player in self.players:
                continue
            self.players.append(player)
            Player.UNIQUE_NAMES.add(player.name)
            added.append(player.name)

        return f"Successfully added: {', '.join(added)}"

    def add_supply(self, *args):
        self.supplies.extend(args)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._find_player(player_name)

        if not player or sustenance_type not in ["Food", "Drink"]:
            ...
        if not player.need_sustenance:
            return f"{player.name} have enough stamina."

        supply_idx, supply = self._get_supply_by_type(sustenance_type)
        self.supplies.pop(supply_idx)

        if not supply:
            raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

        increased_stamina = player.stamina + supply.energy
        player.stamina = increased_stamina if increased_stamina <= 100 else 100
        return f"{player.name} sustained successfully with {supply.name}."


    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self._find_player(first_player_name)
        second_player = self._find_player(second_player_name)

        list_of_players =[first_player, second_player]
        unable_to_start_message = []

        for player in list_of_players:
            if player.stamina == 0:
                unable_to_start_message.append(f"Player {player.name} does not have enough stamina.")
        if unable_to_start_message:
            return '\n'.join(unable_to_start_message)

        sorted_players_by_turn = sorted(list_of_players, key=lambda x: x.stamina)

        winner = ""
        for _ in range(len(sorted_players_by_turn)):
            attacker, defender = sorted_players_by_turn
            reduced_stamina = defender.stamina - attacker.stamina / 2

            if reduced_stamina <= 0:
                defender.stamina = 0
                winner = attacker
                break

            defender.stamina = reduced_stamina
            sorted_players_by_turn = sorted_players_by_turn[::-1]

        if not winner:
            winner = sorted(list_of_players, key=lambda x: x.stamina)[-1]

        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            reduced_stamina = player.stamina - player.age * 2
            player.stamina = reduced_stamina if reduced_stamina >= 0 else 0
            self.sustain(player.name, 'Food')
            self.sustain(player.name, 'Drink')

    def __str__(self):
        output = []
        for player in self.players:
            output.append(str(player))
        for supply in self.supplies:
            output.append(supply.details())
        return '\n'.join(output)