from unittest import TestCase, main
# from lab_files.test_cat import Cat

class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Puffy")

    def test_initialization(self):
        self.assertEqual("Puffy", self.cat.name)

    def test_correct_size_increase_after_eat(self):
        expected_size = self.cat.size+1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)

    def test_fed_cat_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_error_raise_after_fed_cat(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_cannot_sleep_wo_meal_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_not_sleepy_cat_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()