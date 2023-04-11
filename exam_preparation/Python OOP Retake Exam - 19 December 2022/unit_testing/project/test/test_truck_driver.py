from project.truck_driver import TruckDriver
from unittest import TestCase, main


class TestTruckDriver(TestCase):

    def setUp(self) -> None:
        self.driver = TruckDriver("Plamen", 1.20)

    def test_successful_initialization(self):
        self.assertEqual("Plamen", self.driver.name)
        self.assertEqual(1.20, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0.0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_raise_error_when_negative(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -0.1
        self.assertEqual("Plamen went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("Sofia", 2000)

        with self.assertRaises(ValueError) as err:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(err.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_raises_exception_with_duplicating_location(self):
        self.driver.available_cargos["Sofia"] = 100
        self.driver.available_cargos["Varna"] = 4
        self.driver.available_cargos["Plovdiv"] = 60

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 150)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_added_cargo_offers_added_succesfully_(self):
        self.driver.available_cargos["Sofia"] = 100
        self.driver.available_cargos["Varna"] = 4
        self.driver.available_cargos["Plovdiv"] = 60
        result = self.driver.add_cargo_offer("Vidin", 200)
        self.assertEqual(f"Cargo for 200 to Vidin was added as an offer.", result)

        self.assertEqual({"Sofia": 100, "Varna": 4, "Plovdiv": 60, "Vidin": 200}, self.driver.available_cargos)
        self.assertEqual(4, len(self.driver.available_cargos))

    def test_drive_best_cargo_offer_raises_when_no_offers(self):
        result = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", result)

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("Sofia", 200)
        self.driver.add_cargo_offer("Velingrad", 250)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(f"{self.driver.name} is driving 250 to Velingrad.", result)
        self.assertEqual(280.0, self.driver.earned_money)
        self.assertEqual(250, self.driver.miles)

    def test_eat(self):
        self.driver.earned_money = 1000

        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(self.driver.earned_money, 960)

    def test_sleep(self):
        self.driver.earned_money = 1000

        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(self.driver.earned_money, 910)

    def test_pump_gas(self):
        self.driver.earned_money = 1000

        self.driver.pump_gas(1000)
        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)
        self.assertEqual(self.driver.earned_money, 0)

    def test_repair_truck(self):
        self.driver.earned_money = 10000
        self.driver.repair_truck(1000)
        self.driver.repair_truck(10000)
        self.assertEqual(self.driver.earned_money, 2500)

        with self.assertRaises(ValueError) as err:
            self.driver.repair_truck(20000)
        self.assertEqual(str(err.exception), f"{self.driver.name} went bankrupt.")


    def test__repr__(self):
        self.assertEqual("Plamen has 0 miles behind his back.", repr(self.driver))


if __name__ == "__main__":
    main()