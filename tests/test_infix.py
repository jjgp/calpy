from calpy.calculators import infix


def test_parsing_numbers():
    assert infix("3") == 3
    assert infix("32 ") == 32
    assert infix("     321") == 321
    assert infix("   321  ") == 321
    # TODO: support of negative numbers (i.e. "1 -3 +"")? dc does not support this.
