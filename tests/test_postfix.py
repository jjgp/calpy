import pytest

from calpy.calculators import postfix


def test_parsing_numbers():
    assert postfix("3") == 3
    assert postfix("3    2") == 2
    assert postfix("3 2 1") == 1
    assert postfix("     3") == 3
    assert postfix("   1337  ") == 1337
    # TODO: support of negative numbers? dc does not support this.


def test_invalid_inputs():
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("")
    with pytest.raises(ValueError, match="Expression contains unsupported character"):
        postfix("3 (╯°□°)╯︵ ┻━┻ 4")
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("+")
    with pytest.raises(ValueError, match="Expression resulted in empty stack"):
        postfix("21 +")


def test_postfix():
    assert postfix("21 21 +") == 42
