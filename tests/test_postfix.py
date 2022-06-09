import pytest

from calpy.calculators import postfix


def test_parsing_numbers():
    assert postfix("3") == 3
    assert postfix("3    2") == 2
    assert postfix("3 2 1") == 1
    assert postfix("     3") == 3
    assert postfix("   1337  ") == 1337
    assert postfix("_3") == -3


def test_invalid_empty():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("")


def test_invalid_characters():
    with pytest.raises(ValueError, match="Expression contains unsupported character"):
        postfix("3 (╯°□°)╯︵ ┻━┻ 4")


def test_invalid_without_operands():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("+")


def test_invalid_number_of_operands():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("21 +")


def test_simple_expressions():
    assert postfix("21 21 +") == 42
    assert postfix("21 21 -") == 0
    assert postfix("0 1337 +") == 1337
    assert postfix("4 4 *") == 16
    assert postfix("4 2 /") == 2
    assert postfix("5 2 %") == 1


def test_provided_examples():
    assert postfix("5 2 /") == 2
    assert postfix("3 7 *") == 21
    assert postfix("4 7 + 2 *") == 22
    assert postfix("2 3 * 11 14 * +") == 160


def test_no_space_after_operand():
    assert postfix("3 7*20-") == 1


def test_division_by_zero():
    with pytest.raises(ValueError, match="Expression resulted in division by zero"):
        postfix("4 0 /")


def test_modulo_by_zero():
    with pytest.raises(ValueError, match="Expression resulted in remainder by zero"):
        postfix("4 0 %")


def test_negative_sign():
    assert postfix("_5") == -5
    assert postfix("_ 5") == -5
    assert postfix("5_") == 5
    assert postfix("4 5_+") == 9  # TODO: this would be 5 with dc


def test_negative_division():
    assert postfix("_5 2 /") == -2


def test_negative_modulo():
    assert postfix("_ 5 2 %") == -1


def test_complex_expressions():
    assert postfix("0 5 - 2 % 100 * 1337 + 42 54 + /") == 12


def test_fuzzing_expressions():
    """
    TODO: if this was a very secure and mission critical service it would be nice
    to generate or fuzz expressions to check for errors or validity
    """
