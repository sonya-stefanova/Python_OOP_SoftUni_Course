from itertools import permutations


def possible_permutations(elements):
    for num in permutations(elements):
        yield list(num)
