from unit_test_project.shopping_cart import ShoppingCart

from unittest import TestCase


class TestShoppingCart(TestCase):
    def setUp(self):
        self.shopping_cart = ShoppingCart("Lidl", 150)

    def test_init_correct_initialization(self):
        self.assertEqual("Lidl", self.shopping_cart.shop_name, )
        self.assertEqual(150, self.shopping_cart.budget, 150)
        self.assertEqual(0, len(self.shopping_cart.products))

    def test_shop_name_setter_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.shopping_cart.shop_name = "lidl"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.shop_name = "2lidl"
        self.assertEqual("Shop must contain only letters and must start with capital letter!", str(context.exception))

    def test_add_to_cart_product_with_invalid_price_raise_value_erorr(self):
        product_name = "tomato"
        test_price = 150
        with self.assertRaises(ValueError) as context:
            self.shopping_cart.add_to_cart(product_name, test_price)
        self.assertEqual(f"Product {product_name} cost too much!", str(context.exception))

    def test_add_to_cart_successfully_return_string_and_correct_dict(self):
        product_name = "tomato"
        test_price = 8
        result = self.shopping_cart.add_to_cart(product_name, test_price)
        self.assertEqual(f"{product_name} product was successfully added to the cart!", result)
        self.assertEqual(1, len(self.shopping_cart.products))
        self.assertTrue(product_name in self.shopping_cart.products)

    def test_remove_from_cart_raises_exception_when_invalid_product_input(self):
        with self.assertRaises(ValueError) as context:
            self.shopping_cart.remove_from_cart("popcorn")
        self.assertEqual({}, self.shopping_cart.products)
        self.assertEqual(f"No product with name popcorn in the cart!", str(context.exception))


        self.shopping_cart.add_to_cart("popcorn", 10)
        self.shopping_cart.add_to_cart("kiwi", 5)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.remove_from_cart("tomato")
        self.assertEqual(2, len(self.shopping_cart.products))
        self.assertEqual(f"No product with name tomato in the cart!", str(context.exception))

    def test_remove_from_cart_successfully_return_string_and_correct_dict(self):
        self.shopping_cart.add_to_cart("popcorn", 10)
        self.shopping_cart.add_to_cart("kiwi", 5)
        result = self.shopping_cart.remove_from_cart("popcorn")
        self.assertEqual("Product popcorn was successfully removed from the cart!", result)
        self.assertTrue("popcorn" not in self.shopping_cart.products)
        self.assertEqual(1, len(self.shopping_cart.products))

    def test_add_return_new_shopping_cart(self):
        other_shopping_cart = ShoppingCart("Kaufland", 200)
        self.shopping_cart.add_to_cart("product1", 5)
        other_shopping_cart.add_to_cart("product2", 10)
        merged_result = self.shopping_cart.__add__(other_shopping_cart)
        expected = ShoppingCart("LidlKaufland", 350)
        self.assertEqual("LidlKaufland", merged_result.shop_name)
        self.assertEqual(350, merged_result.budget)
        self.assertEqual(2, len(merged_result.products))
        self.assertEqual({"product1": 5, "product2": 10}, merged_result.products)

    def test_buy_products_over_budget_raise_error(self):
        self.shopping_cart.add_to_cart("tomatoes", 99)
        self.shopping_cart.add_to_cart("cucumbers", 91)

        with self.assertRaises(ValueError) as context:
            self.shopping_cart.buy_products()
        self.assertEqual(f"Not enough money to buy the products! Over budget with 40.00lv!", str(context.exception))

    def test_buy_valid_products_with_valid_budget(self):
        self.shopping_cart.add_to_cart("tomatoes", 40)
        self.shopping_cart.add_to_cart("dessert", 50)
        result = self.shopping_cart.buy_products()
        self.assertEqual(f'Products were successfully bought! Total cost: 90.00lv.', result)