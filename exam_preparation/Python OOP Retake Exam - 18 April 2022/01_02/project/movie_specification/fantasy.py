from project.movie_specification.movie import Movie


class Fantasy(Movie):
    AGE_RESTRICTION_GENRE = 6

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = AGE_RESTRICTION_GENRE):
        super().__init__(title, year, owner, age_restriction)