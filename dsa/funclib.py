import random


def gen_list(size=10, scope=(-100, 100), duplicated=False):
    """Generate a random list."""
    start, end = scope
    if duplicated:
        return [random.randint(start, end) for count in range(size)]
    else:
        return random.sample(range(start, end), size)

