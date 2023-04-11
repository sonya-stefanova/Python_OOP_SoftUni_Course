from project.library import Library
from unittest import TestCase

class LibraryTest(TestCase):
    def setUp(self):
        self.library = Library("VarnaLibrabry")

    def test_init_correctness(self):
        self.assertEqual("VarnaLibrabry", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ''
        self.assertEqual("Name cannot be empty string!",str(context.exception))

    def test_add_books_by_author_title_correctness(self):
        author = "Author"
        title = "Title"
        self.assertEqual({}, self.library.books_by_authors)

        self.library.add_book(author, title)
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue("Author" in self.library.books_by_authors)
        self.assertEqual({author: [title]}, self.library.books_by_authors)

        title1 = "Title1"
        self.library.add_book(author, 'Title1')
        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertEqual({author: [title, title1]}, self.library.books_by_authors)

    def test_add_reader_register_name_in_readers_list(self):
        name = "reader"
        self.library.add_reader(name)
        self.assertEqual({"reader": []}, self.library.readers)

    def test_add_already_added_reader_key(self):
        name = "reader"
        self.library.add_reader(name)
        self.assertEqual({"reader": []}, self.library.readers)

        name1 = "reader"
        result = self.library.add_reader(name1)
        self.assertEqual({"reader": []}, self.library.readers)
        self.assertEqual(f"{name} is already registered in the {self.library.name} library.", result)

    def test_rent_book_when_reader_name_not_in_readers_dict(self):
        name = "reader"
        self.library.add_reader(name)
        self.assertEqual({"reader": []}, self.library.readers)

        reader_name = "Sonya"
        book_author = "Ain Rand"
        book_title = "Atlas"
        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)

    def test_rent_book_when_book_author_not_in_authors_dict(self):
        author = "Author"
        title = "Title"
        self.library.add_book(author, title)
        self.assertEqual({author: [title]}, self.library.books_by_authors)

        name = "Sonya"
        self.library.add_reader(name)
        self.assertEqual({name: []}, self.library.readers)

        reader_name = "Sonya"
        book_author = "Ain Rand"
        book_title = "Atlas"
        result = self.library.rent_book(reader_name, book_author, book_title)

        self.assertEqual(f"{self.library.name} Library does not have any {book_author}'s books.", result)

    def test_rent_book_when_book_title_not_in_book_authors_dict(self):
        author = "Ain Rand"
        title = "Title"
        self.library.add_book(author, title)
        self.assertEqual({author: [title]}, self.library.books_by_authors)

        name = "Sonya"
        self.library.add_reader(name)
        self.assertEqual({name: []}, self.library.readers)

        reader_name = "Sonya"
        book_author = "Ain Rand"
        book_title = "Atlas"
        result = self.library.rent_book(reader_name, book_author, book_title)
        self.assertEqual( f"""{self.library.name} Library does not have {book_author}'s "{book_title}".""", result)

    def test_rent_book_successfully(self):
        self.library.add_reader("Sonya")
        self.library.add_book("Ain Rand", "Atlas")
        self.assertEqual({"Ain Rand": ["Atlas"]}, self.library.books_by_authors)
        self.assertEqual({"Sonya": []}, self.library.readers)

        self.library.rent_book("Sonya", "Ain Rand", "Atlas")

        self.assertEqual({"Sonya": [{"Ain Rand": "Atlas"}]}, self.library.readers)
        self.assertEqual({"Ain Rand": []}, self.library.books_by_authors)

