import math

_SUPPORTED_OPERATORS = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int(x / y),
    "%": math.fmod,
}


def _parse_int(expr, from_index):
    to_index = from_index
    while to_index < len(expr) and expr[to_index].isdigit():
        to_index += 1
    return to_index, int(expr[from_index:to_index])


def infix(expr):
    """
    TODO: docstring
    """

    i = 0
    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c.isdigit():
            return _parse_int(expr, i)[1]

        i += 1


def postfix(expr):
    """
    Evaluates a mathematical expression by Reverse Polish notation.
    The solution is both O(n) time and space complexity.

    For more:
        https://en.wikipedia.org/wiki/Reverse_Polish_notation

    :param expr: a string representing the expression to be evaluated
    :returns: the resulting integer value
    :raises ValueError: expressions resulting in empty stacks, for divison or
    remainder by zero, and unsupported characters
    """

    i = 0
    stack = []
    sign = 1
    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c == "_":
            sign = -1
        elif c.isdigit():
            to_index, num = _parse_int(expr, i)
            i = to_index
            stack.append(sign * num)
            sign = 1
        elif c in _SUPPORTED_OPERATORS:
            if len(stack) < 2:
                raise ValueError("Expression resulted in empty stack")
            if c == "/" and stack[-1] == 0:
                raise ValueError("Expression resulted in division by zero")
            if c == "%" and stack[-1] == 0:
                raise ValueError("Expression resulted in remainder by zero")

            y, x = stack.pop(), stack.pop()
            result = _SUPPORTED_OPERATORS[c](x, y)
            stack.append(result)
        else:
            raise ValueError("Expression contains unsupported character")

        i += 1

    if not stack:
        raise ValueError("Expression resulted in empty stack")

    return stack[-1]
