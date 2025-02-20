import random

def get_random_list(size, limit=1000):
    """
    Generates a list of random integers.
    param size: Size of the list.
    :param limit: Maximum value for random integers.
    return: List of random integers.
    """
    return [random.randint(0, limit) for _ in range(size)]
