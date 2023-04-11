from unittest import TestCase, main
# from lab_files.car_manager import Car

class CarManager_Test(TestCase):
    def setUp(self):
        self.car = Car("VW", "Golf Alltrack", 11, 100)

    def test_constructor_correctness(self):
        self.assertEqual("VW", self.car.make)
        self.assertEqual("Golf Alltrack", self.car.model)
        self.assertEqual(11, self.car.fuel_consumption)
        self.assertEqual(100, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_make_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            car = Car("", "Golf Alltrack", 11, 100)

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_empty_model_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raising_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_negative_fuel_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -14

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_return_fuel_capacity(self):
        self.car.refuel(17000)
        self.assertEqual(100, self.car.fuel_capacity)

    def test_add_fuel_less_than_capacity(self):
        extra_fuel = 5
        self.car.refuel(extra_fuel)
        self.assertEqual(extra_fuel, self.car.fuel_amount)

    def test_drive_not_having_enough_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_enough_fuel(self):
        self.car.fuel_amount = 50
        self.car.drive(5)
        self.assertEqual(self.car.fuel_amount, 49.45)

if __name__ == '__main__':
    main()