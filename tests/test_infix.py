import pytest

from calpy.calculators import infix


def test_parsing_numbers():
    assert infix("3") == 3
    assert infix("3    2") == 2
    assert infix("3 2 1") == 1
    assert infix("     3") == 3
    assert infix("   1337  ") == 1337
    assert infix("-3") == -3


def test_invalid_empty():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        infix("")


def test_invalid_characters():
    with pytest.raises(ValueError, match="Expression contains unsupported character"):
        infix("3 (╯°□°)╯︵ ┻━┻ 4")


def test_invalid_without_operands():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        infix("+")


def test_invalid_number_of_operands():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        infix("21 +")


def test_simple_expressions():
    assert infix("21 + 21") == 42
    assert infix("21 - 21") == 0
    assert infix("0 + 1337") == 1337
    assert infix("4 * 4") == 16
    assert infix("4 / 2") == 2
    assert infix("5 / - 4") == -1


def test_provided_examples():
    assert infix("5 / 2") == 2
    assert infix("3 * 7") == 21
    assert infix("(4 + 7) * 2 ") == 22
    assert infix("2 * 3 + 11 * 14") == 160


def test_no_space_around_operators():
    assert infix("3-7*20") == -137


def test_negative_sign():
    assert infix("- - 3") == 3
    assert infix("- (3)") == -3
    assert infix("(- 3)") == -3
    assert infix("1 + (- 3)") == -2
    assert infix("- 3 * 2") == -6
    assert infix("3 * - 2") == -6
    assert infix("- 3 * - 2") == 6
    assert infix("- 3  - - (-2) - 5") == -10


def test_division_by_zero():
    with pytest.raises(ValueError, match="Expression resulted in division by zero"):
        infix("4 / 0")


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Expression resulted in remainder by zero"):
        infix("4 % 0")


def test_negative_division():
    # TODO: this is currently unsupported
    pass


def test_negative_modulo():
    # TODO: this is currently unsupported
    pass


def test_complex_expressions():
    assert infix("((0 - 5) % 2 * 100 + 1337) / (42 + 54)") == 12
