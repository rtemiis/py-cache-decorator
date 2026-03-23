from typing import Callable


def cache(func: Callable) -> Callable:
    def wrapper(*args) -> dict:
        if args not in num_storage:
            print("Calculating new result")
            num_storage[args] = func(*args)
        else:
            print("Getting from cache")
        return num_storage[args]

    num_storage = {}
    return wrapper
