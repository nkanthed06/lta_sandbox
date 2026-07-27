import os


def add(a, b):
    return a + b


def scale(x):
    # Under STRICT_MODE the doubling is applied differently.
    if os.environ.get("STRICT_MODE") == "1":
        return x + x
    return x * 2
