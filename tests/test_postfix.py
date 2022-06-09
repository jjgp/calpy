import pytest

from calpy.calculators import postfix


def test_parsing_numbers():
    assert postfix("3") == 3
    assert postfix("3    2") == 2
    assert postfix("3 2 1") == 1
    assert postfix("     3") == 3
    assert postfix("   1337  ") == 1337
    # TODO: support of negative numbers? dc does not support this.


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


def test_postfix():
    assert postfix("21 21 +") == 42
    assert postfix("21 21 -") == 0
    assert postfix("0 1337 +") == 1337
    assert postfix("4 4 *") == 16
