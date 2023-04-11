from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Sonya", 1, 100, 100)
        self.enemy_hero = Hero("Plamen", 1, 50, 50)

    def test_initializing(self):
        self.assertEqual("Sonya", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_fighting_with_the_same_hero_raises(self):
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_fighting_without_health_equal_zero_raises(self):
        self.hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = "Your health is lower than or equal to 0. " \
                   "You need to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_zero_health_enemy_exception(self):
        self.enemy_hero.health = 0

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_fighting_with_negative_raises(self):
        self.hero.health = -10

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = "Your health is lower than or equal to 0. " \
                   "You need to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_negative_negative_health_enemy_exception(self):
        self.enemy_hero.health = -5

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)

        expected = f"You cannot fight {self.enemy_hero.username}. He needs to rest"
        self.assertEqual(expected, str(ex.exception))

    def test_draw_return(self):
        enemy_hero = Hero("Plamen", 1, 100, 100)
        expected = "Draw"
        result = self.hero.battle(enemy_hero)
        self.assertEqual(expected, result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, enemy_hero.health)

    def test_hero_wins_return(self):
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)
        self.assertEqual(-50, self.enemy_hero.health)
        self.assertEqual(50, self.enemy_hero.damage)

    def test_damage_and_health_change_return_win_enemy(self):
        hero = Hero("S", 1, 100, 40)
        enemy = Hero("P", 1, 100, 50)

        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(2, enemy.level)
        self.assertEqual(65, enemy.health)
        self.assertEqual(55, enemy.damage)
        self.assertEqual(50, hero.health)


    def test__str__representation_correctness(self):
        expected_output = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"

        self.assertEqual(expected_output, str(self.hero))
if __name__ == '__main__':
    main()