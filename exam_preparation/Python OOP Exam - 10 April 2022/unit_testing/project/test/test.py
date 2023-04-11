from unittest import TestCase, main

from project.movie import Movie

class MovieTest(TestCase):
    def setUp(self):
        self.movie = Movie('The Shawshank Redemption', 1994, 10)

    def test_init(self):
        self.assertEqual(self.movie.name, 'The Shawshank Redemption')
        self.assertEqual(self.movie.year, 1994)
        self.assertEqual(self.movie.rating, 10)
        self.assertEqual([], self.movie.actors)

    def test_property_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test_property_year_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.movie.year = 1880

        self.assertEqual("Year is not valid!", str(context.exception))

    def test_add_actor_if_not_in_the_list(self):
        actor_name = "Jane Austin"
        result = self.movie.add_actor(actor_name)
        self.assertEqual(1, len(self.movie.actors))
        self.assertEqual(["Jane Austin"], self.movie.actors)

    def test_add_actor_if_in_the_list(self):
        self.movie.actors = ["actor1", "actor2", "actor3"]
        actor_name = "actor1"
        result = self.movie.add_actor(actor_name)
        self.assertEqual(3, len(self.movie.actors))
        self.assertEqual(["actor1", "actor2", "actor3"], self.movie.actors)
        self.assertEqual(f"{actor_name} is already added in the list of actors!", result)

    def test_gt_better_rating(self):
        movie2 = Movie("Movie2", 1991, 3.8)
        result = self.movie.__gt__(movie2)
        self.assertTrue(result)
        self.assertEqual(f'"The Shawshank Redemption" is better than "Movie2"', result)

    def test_get_less_rating(self):
        other = Movie("Other", 2006, 15)

        result = self.movie.__gt__(other)

        self.assertEqual(f'"{other.name}" is better than "{self.movie.name}"', result)

    def test_repr_correctness(self):
        self.movie.add_actor("Adam Sandler")
        self.movie.add_actor("Sean Pen")
        self.movie.add_actor("Brad Pit")
        result = repr(self.movie)
        expected = f"Name: The Shawshank Redemption\n" \
               f"Year of Release: 1994\n" \
               f"Rating: 10.00\n" \
               f"Cast: Adam Sandler, Sean Pen, Brad Pit"
        self.assertEqual(expected, result)
