from unittest import TestCase, main
from lab_files.test_worker import Worker

class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("Sonya", 2000, 100)

    def test_correct_initialization(self):
        self.assertEqual("Sonya", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)

    def test_work_energy_increase(self):
        resultative_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(resultative_energy, self.worker.energy)

    def test_zero_energy_raise_exception(self):
        worker = Worker("Sonya", 2000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_correct_salary_increase(self):
        expected_money = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)

    def test_correct_energy_decrease(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_returning_of_correct_string(self):
        expected_str = f"{self.worker.name} has saved {self.worker.money} money."
        actual_str = self.worker.get_info()
        self.assertEqual(expected_str, actual_str)

if __name__ == "__main__":
    main()