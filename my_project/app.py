"""Main application module."""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


if __name__ == "__main__":
    print("Add 5 + 3 =", add(5, 3))
    print("Subtract 5 - 3 =", subtract(5, 3))
