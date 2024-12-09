import re

def add(a: int | float, b: int | float) -> int | float:
    """Adds two values.

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a + b


def minus(a: int | float, b: int | float) -> int | float:
    """Minus operator. Deducts b from a

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a - b


def divide(a: int | float, b: int | float) -> int | float:
    """Division operator. Divides a by b

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a / b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplier operator. Multiplies a by b

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a * b


def modulo(a: int | float, b: int | float) -> int | float:
    """Modulo operator. Returns the remainder of a/b

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a % b


def integer_divide(a: int | float, b: int | float) -> int | float:
    """Returns the integer after dividing a by b

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a // b


def exponent(a: int | float, b: int | float) -> int | float:
    """Exponent operator. Returns a raised to the power of b

    Args:
        a (int | float)
        b (int | float)

    Returns:
        int | float
    """
    return a**b

def string_add(a: str, b: str) -> str:
    """String concatenator. Returns a concatenated string 
    with an additional space

    Args:
        a (str) 
        b (str)

    Returns:
        str
    """
    return a + " "+ b

def string_remove(a: str, b: str) -> str:
    """Removes string pattern b from a

    Args:
        a (str)
        b (str)

    Returns:
        str
    """
    try:
        return re.sub(b, '', a)
    except Exception as e:
        return e