from calpy.calculators import postfix


def test_parsing_numbers():
    assert postfix("3") == 3
    assert postfix("3    2") == 2
    assert postfix("3 2 1") == 1
    assert postfix("     3") == 3
    assert postfix("   1337  ") == 1337
    # TODO: testing of negative numbers? dc does not support this


def test_postfix():
    assert postfix("21 21 +") == 42
