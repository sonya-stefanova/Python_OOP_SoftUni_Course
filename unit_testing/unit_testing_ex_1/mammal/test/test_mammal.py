from unittest import TestCase, main
from project.mammal import Mammal

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("lion", "cats", "meaow")

    def test_constructor_correctness(self):
        self.assertEqual("lion",self.mammal.name)
        self.assertEqual("cats", self.mammal.type)
        self.assertEqual("meaow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_correctness(self):
        result = self.mammal.make_sound()
        self.assertEqual("lion makes meaow", result)

    def test_get_kingdom_correctness(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_correctness(self):
        result = self.mammal.info()
        self.assertEqual("lion is of type cats", result)