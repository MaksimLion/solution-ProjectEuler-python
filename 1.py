def is_multiple(number, args):
    for i in args:
        if number % i == 0:
            return True


def multiple_numbers(numbers, *args):
    numbers_list = [number for number in range(numbers)]
    multiple_numbers = []
    for i in numbers_list:
        if is_multiple(i, args):
            multiple_numbers.append(i)
    print(multiple_numbers)
    return multiple_numbers


def task1():
    return sum(multiple_numbers(10, 3, 5))

