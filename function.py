from time import time
from decimal import Decimal


def sieve(n: int) -> list:
    """Function that implements the sieve of Eratosthenes"""
    # Make sure that n is a number
    try:
        n = int(n)
    except ValueError:
        print("Given input is not a number!")
        return []

    # Make sure user specified correct number, because prime numbers start from 2.
    # It also needs to be bigger than 0 to perform sqrt().
    if n < 2:
        print("Given number: " + str(n) + ", is too small!")
        return []

    # Time measure
    start = Decimal(time())

    # All the numbers that we want to check
    numbers = list(range(2, n + 1))

    # The number that we want to end iteration on
    n = round(n ** 0.5)

    # The range of numbers that we have to check
    search_range = list(range(2, n + 1))

    for i in search_range:
        for j in numbers:
            if j % i == 0 and j != i:
                del numbers[numbers.index(j)]

                # For optimization purposes we check if this number exists in our search_range list, if so we
                # delete it and now program has to check less numbers
                if j in search_range:
                    del search_range[search_range.index(j)]

    # Time measure
    print("Time:", Decimal(time()) - start, "sec")

    return numbers
