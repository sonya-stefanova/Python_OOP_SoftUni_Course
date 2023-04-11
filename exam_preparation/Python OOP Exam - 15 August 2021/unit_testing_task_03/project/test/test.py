from project.pet_shop import PetShop
from unittest import TestCase


class PetShopTests(TestCase):
    def setUp(self) -> None:
        self.pet_shop = PetShop("MyPetShop")

    def test_initialisation_correctness(self):
        self.assertEqual("MyPetShop", self.pet_shop.name)
        self.assertEqual({}, self.pet_shop.food)
        self.assertEqual([], self.pet_shop.pets)

    def test_add_food_qty_negative_raise(self):
        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("meet", 0)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.pet_shop.add_food("meet", -1)

    def test_add_food_to_food_dict_return(self):
        food_name = "fish"
        quantity = 40
        actual_result = self.pet_shop.add_food(food_name, quantity)
        expected_result = f"Successfully added {quantity:.2f} grams of {food_name}."
        self.assertEqual(expected_result, actual_result)
        self.assertTrue({"fish": 40})
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertTrue(quantity, self.pet_shop.food[food_name])

    def test_add_quantity_to_exst_food(self):
        food_name = "fish"
        quantity_initial = 40
        self.pet_shop.food[food_name] = quantity_initial
        add_quantity = 50
        result = self.pet_shop.add_food(food_name, quantity_initial)
        expected = 90
        self.assertEqual(f"Successfully added 40.00 grams of {food_name}.", result)
        self.assertTrue(food_name in self.pet_shop.food)
        self.assertTrue(quantity_initial+add_quantity, self.pet_shop.food[food_name])

    def test_add_pet_raises_error(self):
        pet_name = "Bob"
        self.pet_shop.pets.append(pet_name)
        with self.assertRaises(Exception) as ex:
            self.pet_shop.add_pet("Bob")

        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_pet_appended_successfully_return(self):
        pet_name= "Bob"
        result = self.pet_shop.add_pet(pet_name)
        self.assertIn(pet_name, self.pet_shop.pets)
        self.assertEqual(f"Successfully added {pet_name}.", result)

    def test_feed_pet_if_pet_not_in_pets_raises(self):
        with self.assertRaises(Exception) as ex:
            self.pet_shop.feed_pet("fish", "Gosho")

        self.assertEqual("Please insert a valid pet name", str(ex.exception))

    def test_feed_pet_raises_ex_when_food_doesnt_exist(self):
        pet_name = "Pipi"
        self.pet_shop.pets.append(pet_name)

        result = self.pet_shop.feed_pet("fish", pet_name)
        self.assertEqual(f'You do not have fish', result)

    def test_feed_pet_less_than_100_return(self):
        pet_name = "Pipi"
        food_name = "fish"
        initial_qty = 30
        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name]=initial_qty
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual(initial_qty+1000 , self.pet_shop.food[food_name])

    def test_feed_pet_when_qty_is_equal_more_than_100_return(self):
        pet_name = "Pipi"
        food_name = "fish"
        initial_qty = 190
        self.pet_shop.pets.append(pet_name)
        self.pet_shop.food[food_name] = initial_qty
        result = self.pet_shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(initial_qty - 100, self.pet_shop.food[food_name])

    def test_repr_method_return(self):
        self.pet_shop.pets.append("Pipi")
        self.pet_shop.pets.append("Mimi")

        result = repr(self.pet_shop)
        expected = f'Shop MyPetShop:\n' \
               f'Pets: Pipi, Mimi'
        self.assertEqual(expected, result)
