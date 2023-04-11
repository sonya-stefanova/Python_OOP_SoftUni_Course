from unittest import TestCase, main
from project.team import Team

class TeamTest(TestCase):

    def setUp(self) -> None:
        self.team = Team("BestTeam")

    def test_init_is_correctly_initilised(self):
        self.assertEqual("BestTeam", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_raises_when_value_is_not_alpha(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = "Best_1r3tur$$"

        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test_setter_proper_alphabetic_only_name(self):
        self.team.name = "Team"
        self.assertEqual("Team", self.team.name)

    def test_add_new_members_only(self):
        self.team.members["Gosho"] = 18
        result = self.team.add_member(Gosho=18, Ivan=15, Peter=22)
        self.assertEqual(f'Successfully added: Ivan, Peter', result)
        self.assertEqual(3, len(self.team.members))
        self.assertEqual(18, self.team.members["Gosho"])
        self.assertEqual(15, self.team.members["Ivan"])
        self.assertEqual(22, self.team.members["Peter"])
        self.assertEqual({"Gosho": 18, "Ivan": 15, "Peter": 22}, self.team.members)

    def test_remove_member_return_error_message(self):
        self.team.members["Ivan"] = 15
        self.team.members["Petya"] = 18
        self.assertNotIn("Gosho", self.team.members)
        result = self.team.remove_member("Gosho")
        self.assertEqual(f"Member with name Gosho does not exist", result)

    def test_remove_member_correctness_return_removed_successfully(self):
        self.team.add_member(petar=16, ivan=14,plamen=25)
        result = self.team.remove_member("ivan")
        self.assertEqual(f'Member ivan removed', result)
        self.assertNotIn("ivan", self.team.members)
        self.assertEqual(2, len(self.team.members))
        self.assertEqual({"petar": 16, "plamen": 25}, self.team.members)

    def test_gt_compares_team_by_members_count(self):
        self.team.add_member(Ivan=18, Petya=19)
        other_team = Team("Teamother")
        other_team.add_member(Ivan=19)
        self.assertEqual(True, self.team>other_team)
        self.assertFalse(self.team<other_team)

    def test_len_return(self):
        self.team.add_member(Ivan=18, Petya=19)
        result = len(self.team)
        self.assertEqual(2, result)

    def test_return_team_combination(self):
        other_team = Team("Teamother")

        self.team.add_member(Ivan=18, Petya=19)
        other_team.add_member(Silviya=19, Plamen=20)

        new_team = self.team+other_team
        self.assertEqual("BestTeamTeamother", new_team.name)
        self.assertEqual(4, len(new_team.members))
        self.assertEqual({"Ivan": 18, "Petya":19, "Silviya": 19, "Plamen": 20}, new_team.members)

    def test_str_return(self):
        self.team.members = {"Petya": 18, "Gosho": 15, "Maria": 15}
        result = "Team name: BestTeam\n" \
                 "Member: Petya - 18-years old\n" \
                 "Member: Gosho - 15-years old\n" \
                 "Member: Maria - 15-years old"
        self.assertEqual(result, str(self.team))

if __name__ == "__main__":
    main()