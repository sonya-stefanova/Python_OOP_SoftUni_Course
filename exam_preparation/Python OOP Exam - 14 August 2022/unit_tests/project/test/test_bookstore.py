from project.bookstore import Bookstore

from unittest import TestCase


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.book_store = Bookstore(10)

    def test_init_correctness(self):
        self.assertEqual(10, self.book_store.books_limit)
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.book_store._Bookstore__total_sold_books)

    def test_books_limit_setter_raises_exception_if_zero_value(self):
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(error.exception))

    def test_books_limit_setter_raises_exception_if_negative_value(self):
        with self.assertRaises(ValueError) as error:
            self.book_store.books_limit = -1

        self.assertEqual("Books limit of -1 is not valid", str(error.exception))

    def test_return_total_books_in_bookstore(self):
        self.book_store.availability_in_store_by_book_titles["book1"] = 5
        self.book_store.availability_in_store_by_book_titles["book2"] = 1
        result = len(self.book_store)
        self.assertEqual(6, result)

    def test_raises_exception_if_space_limit_reached(self):
        with self.assertRaises(Exception) as error:
            self.book_store.receive_book("book1", 111)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(error.exception))

    def test_receive_book_if_enough_space_return_total_book_copies(self):
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)
        self.book_store.availability_in_store_by_book_titles["book1"] = 5
        result = self.book_store.receive_book("book1", 1)
        self.assertEqual("6 copies of book1 are available in the bookstore.", result)
        self.assertEqual({"book1": 6}, self.book_store.availability_in_store_by_book_titles)
        self.assertTrue("book1" in self.book_store.availability_in_store_by_book_titles)

    def test_sell_book_raises_exception_if_book_not_available(self):
        self.assertEqual({}, self.book_store.availability_in_store_by_book_titles)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("book1", 1)

        self.assertEqual("Book book1 doesn't exist!", str(error.exception))

    def test_sell_book_raise_exception_if_not_enough_copies(self):
        self.book_store.receive_book("Test_book", 5)

        with self.assertRaises(Exception) as error:
            self.book_store.sell_book("Test_book", 50)

        self.assertEqual(f"Test_book has not enough copies to sell. Left: 5", str(error.exception))
        self.assertEqual({"Test_book": 5}, self.book_store.availability_in_store_by_book_titles)
        self.assertIn("Test_book", self.book_store.availability_in_store_by_book_titles)

    def test_sell_book_successfully_return_total_sold_books(self):
        test_book = "Test_book"
        received_books = self.book_store.receive_book("Test_book", 5)
        self.assertEqual(5, len(self.book_store))

        sold_books = self.book_store.sell_book("Test_book", 4)

        self.assertIn("Test_book", self.book_store.availability_in_store_by_book_titles)
        self.assertEqual(4, self.book_store._Bookstore__total_sold_books)
        self.assertEqual(f"Sold 4 copies of {test_book}", sold_books)

    def test_correct_book_str_representation(self):
        self.book_store.receive_book("book1", 1)
        self.book_store.receive_book("book2", 2)
        self.book_store.receive_book("book3", 2)
        self.book_store.sell_book("book3", 2)
        expected = 'Total sold books: 2\n' \
                   'Current availability: 3\n' \
                   ' - book1: 1 copies\n' \
                   ' - book2: 2 copies\n' \
                   ' - book3: 0 copies'
        self.assertEqual(expected, str(self.book_store))