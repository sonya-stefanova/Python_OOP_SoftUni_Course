from unittest import TestCase, main
# from lab_files.extended_list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList('199', 1, True, 7.185, 2, 3)

    def test_initializing(self):
        expected_list = [1, 2, 3]
        actual_list = self.integer_list.get_data()
        self.assertEqual(expected_list, actual_list)

    def test_add_list_change(self):
        expected = self.integer_list.get_data()+[5]
        self.integer_list.add(5)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_add_operation_ve(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.add("fhdgfd")

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_index_operation_correct_return(self):
        expected = 2
        self.assertEqual(expected, self.integer_list.remove_index(1))

    def test_remove_index_operation_list_after_removing(self):
        expected = [1, 3]
        self.integer_list.remove_index(1)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_remove_index_operation_ie(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.remove_index(15)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_return(self):
        expected = 2
        self.assertEqual(expected, self.integer_list.get(1))

    def test_get_index_ie(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.get(15)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_valid_index_and_type_return(self):
        expected = [1, 2, 4, 3]
        self.integer_list.insert(len(self.integer_list.get_data()) - 1, 4)
        self.assertEqual(expected, self.integer_list.get_data())

    def test_insert_ie(self):
        with self.assertRaises(IndexError) as ex:
            self.integer_list.insert(100, 100)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_ve(self):
        with self.assertRaises(ValueError) as ex:
            self.integer_list.insert(1, 7.1899)

        self.assertEqual("Element is not Integer", str(ex.exception))


    def test_get_max(self):
        exp_rest = 3
        self.assertEqual(exp_rest, self.integer_list.get_biggest())

    def test_get_idx(self):
        exp_res = 0
        self.assertEqual(exp_res, self.integer_list.get_index(1))



if __name__ == '__main__':
    main()