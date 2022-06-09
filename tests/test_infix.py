import pytest

from calpy.calculators import infix


def test_infix_not_implemented():
    with pytest.raises(
        NotImplementedError, match="Infix notation is not yet supported"
    ):
        infix("")
