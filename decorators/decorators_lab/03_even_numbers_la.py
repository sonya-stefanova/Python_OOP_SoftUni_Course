from functools import wraps


def even_numbers(function):

    def is_even(num):
        return num % 2 == 0

    @wraps(function)
    def wrapper(numbers):  # *arg
        result = function(numbers)
        # return [num for num in numbers if is_even(num)]
        return list(filter(is_even, numbers))

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
