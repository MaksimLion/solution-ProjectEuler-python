def is_simple_number(number):
    return all(number % i for i in range(2,number))


def get_all_simple_dividers(number):
    pass