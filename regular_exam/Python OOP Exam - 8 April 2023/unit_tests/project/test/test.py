from unittest import TestCase

from project.tennis_player import TennisPlayer

class TennisPlayerTest(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Sonya", 34, 100)

    def test_init_correctness(self):
        self.assertEqual("Sonya", self.tennis_player.name)
        self.assertEqual(34, self.tennis_player.age)
        self.assertEqual(100, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_setter_raises(self):
        with self.assertRaises(ValueError) as context:
            self.tennis_player.name = 'x'
        self.assertEqual("Name should be more than 2 symbols!", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.tennis_player.name = 'xx'
        self.assertEqual("Name should be more than 2 symbols!", str(context.exception))

    def test_name_setter_correctness(self):
        self.tennis_player.name = 'Testname'
        self.assertEqual("Testname", self.tennis_player.name)

    def test_age_setter_raises_ve(self):
        with self.assertRaises(ValueError) as context:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(context.exception))

    def test_age_correct_initialization(self):
        self.tennis_player.age = 22
        self.assertEqual(22, self.tennis_player.age)

    def test_add_new_win_success(self):
        tournament_name = "test_tournament_name"
        result = self.tennis_player.add_new_win(tournament_name)
        self.assertEqual(["test_tournament_name"], self.tennis_player.wins)
        self.assertEqual(1, len(self.tennis_player.wins))
        self.assertIn("test_tournament_name", self.tennis_player.wins)

    def test_add_already_added_win_return(self):
        self.tennis_player.add_new_win("test_tournament_name")
        result = self.tennis_player.add_new_win("test_tournament_name")
        self.assertEqual(1, len(self.tennis_player.wins))
        self.assertEqual("test_tournament_name has been already added to the list of wins!", result)

    def test_lt_self_points(self):
        other_tennis_player = TennisPlayer("Test", 22, 101)
        result = self.tennis_player.points<other_tennis_player.points
        self.assertEqual(True, result)
        self.assertEqual("Test is a top seeded player and he/she is better than Sonya",
                         self.tennis_player.__lt__(other_tennis_player))

        other_tennis_player = TennisPlayer("Test", 22, 99)
        result = self.tennis_player.points<other_tennis_player.points
        self.assertEqual(False, result)
        self.assertEqual('Sonya is a better player than Test',
                         self.tennis_player.__lt__(other_tennis_player))

    def test_str_correctness(self):
        self.tennis_player.add_new_win("test")
        self.tennis_player.add_new_win("test1")
        result = self.tennis_player.__str__()
        expected = f"Tennis Player: Sonya\n" \
               f"Age: 34\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: test, test1"

        self.assertEqual(expected,result)

    def test_str_correctness_without_wins(self):
        result = self.tennis_player.__str__()
        expected = f"Tennis Player: Sonya\n" \
               f"Age: 34\n" \
               f"Points: 100.0\n" \
               f"Tournaments won: "

        self.assertEqual(expected,result)