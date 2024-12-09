from main import add, minus, divide, modulo, integer_divide, exponent

a = 12
b = 3


def test_add():
    assert add(a, b) == 15


def test_exponent():
    assert exponent(a, b) == 1728


def test_integer_divide():
    assert integer_divide(a, b) == 4


def test_divide():
    assert divide(a, b) == 4


def test_modulo():
    assert modulo(a, b) == 0


def test_minus():
    assert minus(a, b) == 9
