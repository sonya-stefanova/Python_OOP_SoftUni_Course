from project.toy_store import ToyStore
from unittest import TestCase

class TestToyStore(TestCase):
    def setUp(self):
        self.toy_store = ToyStore()

    def test_init_correctness(self):
        self.assertIsInstance(self.toy_store, ToyStore)
        self.assertEqual(7, len(self.toy_store.toy_shelf))
        self.assertIn("A", self.toy_store.toy_shelf)
        self.assertIn("B", self.toy_store.toy_shelf)
        self.assertIn("C", self.toy_store.toy_shelf)
        self.assertIn("D", self.toy_store.toy_shelf)
        self.assertIn("E", self.toy_store.toy_shelf)
        self.assertIn("F", self.toy_store.toy_shelf)
        self.assertIn("G", self.toy_store.toy_shelf)
        self.assertIn(None, self.toy_store.toy_shelf.values())

        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None}, self.toy_store.toy_shelf)

    def test_add_toy_raises_exception_shelf_not_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("M", "Puffy")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_toy_added_succesffully(self):
        result = self.toy_store.add_toy("A", "Puffy")
        self.assertEqual(f"Toy:Puffy placed successfully!", result)

    def test_add_raises_exception_already_added_toy(self):
        result = self.toy_store.add_toy("A", "Puffy")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Holly")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_already_added_toy_raising_exception(self):
        result = self.toy_store.add_toy("A", "Puffy")

        with self.assertRaises(Exception) as ex:
            self.toy_store.add_toy("A", "Puffy")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_remove_toy_raises_when_shelf_doesnt_exist(self):
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("M", "Puffy")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))
        self.assertEqual(7, len(self.toy_store.toy_shelf))

    def test_remove_toy_raises_exception_when_toy_does_not_exist(self):
        self.toy_store.add_toy("A", "Puffy")
        with self.assertRaises(Exception) as ex:
            self.toy_store.remove_toy("A", "Pilly")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_remove_tou_successfully(self):
        self.toy_store.add_toy("A", "Puffy")
        result = self.toy_store.remove_toy("A", "Puffy")
        self.assertEqual(f"Toy:Puffy removed successfully!", result)
        self.assertEqual(6, len(self.toy_store.toy_shelf))
        self.assertNotIn("A", self.toy_store.toy_shelf)
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy_store.toy_shelf)