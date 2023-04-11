from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory

class FactoryTest(TestCase):
    def setUp(self) -> None:
        self.paint_factory = PaintFactory('name', 10)

    def test_init(self):
        self.assertEqual('name', self.paint_factory.name)
        self.assertEqual(10, self.paint_factory.capacity)

    def test_valid_ingredients(self):
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.paint_factory.valid_ingredients)

    def test_valid_ingredients_dictionary(self):
        self.assertEqual({}, self.paint_factory.ingredients)

    def test_add_ingredients_if_type_not_in_ingredients_list(self):
        with self.assertRaises(TypeError) as ex:
            self.paint_factory.add_ingredient('invalid', 5)
        self.assertEqual(f"Ingredient of type invalid not allowed in {self.paint_factory.__class__.__name__}", str(ex.exception))

    def test_add_ingredient_if_can_add_return_false(self):
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.add_ingredient('white', 11)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_if_product_type_is_in_ingredients_dict(self):
        self.paint_factory.ingredients["white"] = 2
        self.assertEqual({'white':2}, self.paint_factory.ingredients)
        self.paint_factory.add_ingredient('white', 2)
        self.assertEqual({'white':4}, self.paint_factory.ingredients)
        self.assertEqual(4, self.paint_factory.ingredients["white"])

    def test_add_ingredient_when_can_add_if_product_type_is_not_in_ingredients_dict(self):
        self.paint_factory.ingredients["white"] = 2
        self.assertEqual(2, self.paint_factory.ingredients["white"])

    def test_add_ingredient(self):
        self.paint_factory.add_ingredient('white', 10)
        self.assertEqual({'white': 10}, self.paint_factory.ingredients)

    def test_can_add_is_zero(self):
        self.paint_factory.ingredients["white"] = 8
        self.assertEqual(True, self.paint_factory.can_add(2))
        # return self.capacity - sum(self.ingredients.values()) - value >= 0
    def test_can_add_is_positive(self):
        self.paint_factory.ingredients["white"] = 2
        self.assertEqual(True, self.paint_factory.can_add(2))
        # return self.capacity - sum(self.ingredients.values()) - value > 0

    def test_can_add_is_negative(self):
        self.paint_factory.ingredients["white"] = 10
        self.assertEqual(False, self.paint_factory.can_add(2))
        # return self.capacity - sum(self.ingredients.values()) - value >= 0

    def test_remove_if_product_type_not_in_ingredients_dictionary(self):
        with self.assertRaises(KeyError) as ex:
            self.paint_factory.remove_ingredient('invalid', 5)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_if_quantity_is_negative(self):
        self.paint_factory.ingredients["white"] = 8
        with self.assertRaises(ValueError) as ex:
            self.paint_factory.remove_ingredient("white", 9)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_if_quantity_is_correct(self):
        self.paint_factory.ingredients["white"] = 8
        self.paint_factory.remove_ingredient("white", 8)
        self.assertEqual(0, self.paint_factory.ingredients["white"])

    def test_products_property(self):
        self.paint_factory.add_ingredient('white', 10)
        self.assertEqual({'white': 10}, self.paint_factory.products)

if __name__ == '__main__':
    main()