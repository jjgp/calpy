from calpy.calculators import postfix


def test_postfix():
    assert postfix("21 21 +") == 42
