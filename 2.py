def is_even(number):
    return number % 2 == 0


def get_even_fibonachi_numbers(limit):
    fib1 = fib2 = 1
    fibonachi = [fib1]
    while fib1 < limit:
        fib1, fib2 = fib2, fib1 + fib2
        if is_even(fib1):
            fibonachi.append(fib1)
    return fibonachi


def task2():
    return sum(get_even_fibonachi_numbers(4000000))
        
