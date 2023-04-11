from decorators.func_even_numbers import func_even_numbers


@func_even_numbers
def get_numbers(nums):
    return nums

print(get_numbers([1,2,3,4,5,6,7,8,9,10]))