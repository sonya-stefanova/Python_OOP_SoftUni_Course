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

    def test_add_toy_raises_exception_shelf_not_exist(self):
        shelf = "M"
        toy_name = "Doll"
        with self.assertRaises(Exception) as exception:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual("Shelf doesn't exist!", str(exception.exception))

    def test_add_toy_raises_exception_toy_already_exist(self):
        shelf = "D"
        toy_name = "Doll"
        self.toy_store.add_toy(shelf, toy_name)
        test_toy_name = "Doll"
        with self.assertRaises(Exception) as exception:
            self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual("Toy is already in shelf!", str(exception.exception))
        self.assertNotEqual(None, self.toy_store.toy_shelf[shelf])
        self.assertEqual(test_toy_name, self.toy_store.toy_shelf[shelf])

    def test_add_toy_raises_exception_shelf_already_taken(self):
        toy_name = "Doll"
        self.toy_store.toy_shelf["D"] = toy_name

        with self.assertRaises(Exception) as exception:
            self.toy_store.add_toy("D", "Bear")

        self.assertEqual("Shelf is already taken!", str(exception.exception))
        self.assertEqual(toy_name,self.toy_store.toy_shelf["D"])
        self.assertNotIn("Bear",self.toy_store.toy_shelf.values())

    def test_add_toy_return_successful_string(self):
        toy_name = "Python"
        shelf = "D"
        result = self.toy_store.add_toy(shelf, toy_name)
        self.assertEqual(f"Toy:{toy_name} placed successfully!", result)

    def test_remove_toy_raise_exception_when_shelf_doesnt_exist(self):
        shelf = "M"
        toy_name = "Doll"
        with self.assertRaises(Exception) as exception:
            self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual("Shelf doesn't exist!", str(exception.exception))
        self.assertNotIn(shelf, self.toy_store.toy_shelf.keys())
        self.assertEqual(7, len(self.toy_store.toy_shelf))

    def test_remove_raises_ex_when_toy_doesnt_exist(self):
        shelf = "D"
        toy_name = "Doll"
        with self.assertRaises(Exception) as exception:
            self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual("Toy in that shelf doesn't exists!", str(exception.exception))
        self.assertNotIn(toy_name, self.toy_store.toy_shelf.values())
        self.assertEqual(7, len(self.toy_store.toy_shelf))

    def test_remove_toy_return_successful_string(self):
        self.toy_store.add_toy("D", "Doll")
        shelf = "D"
        toy_name = "Doll"
        result = self.toy_store.remove_toy(shelf, toy_name)
        self.assertEqual(None, self.toy_store.toy_shelf[shelf])
        self.assertNotIn(toy_name, self.toy_store.toy_shelf.values())
        self.assertEqual(f"Remove toy:{toy_name} successfully!", result)