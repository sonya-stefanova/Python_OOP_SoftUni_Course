# from testing.project.train.train import Train

from project.train.train import Train

from unittest import TestCase

class TrainTests(TestCase):
    def setUp(self) -> None:
        self.train = Train("Train", 3)

    def test_init_correctness(self):
        self.assertEqual("Train", self.train.name)
        self.assertEqual(3, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_class_attributes_correctness(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_add_when_capacity_is_full_raise_error(self):
        self.train.passengers = ["Ivan", "Petkan", "Simeon"]

        with self.assertRaises(ValueError) as error:
            self.train.add("Sonya")

        self.assertEqual(self.train.TRAIN_FULL, str(error.exception))

        self.train.passengers = ["a", "b"]
        with self.assertRaises(ValueError) as error:
            self.train.add("Sonya")
            self.train.add("Mitko")
            self.train.add("Pitko")

        self.assertEqual(self.train.TRAIN_FULL, str(error.exception))

    def test_add_if_passenger_exist_raise_error(self):
        passenger_name = "Ivan"
        self.train.passengers = [passenger_name]

        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)

        self.assertEqual(f"Passenger {passenger_name} Exists", str(error.exception))
        self.assertEqual(1, len(self.train.passengers))

    def test_add_passenger_successfully(self):
        passenger_name = "Sonya"
        result = self.train.add(passenger_name)
        result = self.train.add("Petkan")

        self.assertEqual(f"Added passenger {passenger_name}", result)
        self.assertTrue(passenger_name in self.train.passengers)
        self.assertEqual(1, len(self.train.passengers))
        self.assertEqual(["Sonya", "Petkan"], self.train.passengers)

    def test_remove_passenger_name_if_does_not_exist_raise_error(self):
        self.train.add("Ivan")
        not_existing_passenger_name = "Sonya"

        with self.assertRaises(ValueError) as error:
            self.train.remove(not_existing_passenger_name)

        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_successfully_removed_passenger(self):
        existing_passenger_name = "Sonya"
        self.train.add(existing_passenger_name)

        result = self.train.remove(existing_passenger_name)

        self.assertEqual(f"Removed {existing_passenger_name}", result)
