from project.movie_specification.movie import Movie


class Thriller(Movie):
    AGE_RESTRICTION_GENRE = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = AGE_RESTRICTION_GENRE):
        super().__init__(title, year, owner, age_restriction)