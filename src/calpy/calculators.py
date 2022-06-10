import math
from collections import defaultdict

_OPS_SUPPORTED = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: int(x / y),
    "%": math.fmod,
}

_OPS_PRECEDENCE = defaultdict(
    int,
    {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "%": 2,
    },
)


def _apply_operator(op, outputs):
    if op not in _OPS_SUPPORTED:
        raise ValueError("Expression contains unsupported character")
    elif len(outputs) < 2:
        raise ValueError("Expression resulted in empty stack")
    elif op == "/" and outputs[-1] == 0:
        raise ValueError("Expression resulted in division by zero")
    elif op == "%" and outputs[-1] == 0:
        raise ValueError("Expression resulted in remainder by zero")

    y, x = outputs.pop(), outputs.pop()
    result = _OPS_SUPPORTED[op](x, y)
    outputs.append(result)


def _parse_num(expr, from_index):
    num = 0
    while from_index < len(expr) and expr[from_index].isdigit():
        num = 10 * num + int(expr[from_index])
        from_index += 1
    from_index -= 1
    return num, from_index


def infix(expr):
    """
    Evaluates a mathematical expression by infix notation.
    The solution is both O(n) time and space complexity.

    The solution was aided by:
        https://www.geeksforgeeks.org/expression-evaluation/

    :param expr: a string representing the expression to be evaluated
    :returns: the resulting integer value
    :raises ValueError: expressions resulting in empty stacks, for divison or
    remainder by zero, and unsupported characters
    """

    i = 0
    ops = []
    outputs = []
    sign = 1

    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c.isdigit():
            num, i = _parse_num(expr, i)
            outputs.append(sign * num)
            sign = 1
        elif c == "(":
            ops.append(c)
        elif c == ")":
            while ops and ops[-1] != "(":
                _apply_operator(ops.pop(), outputs)
            ops.pop()
        elif c == "-" and len(outputs) <= len(ops):
            sign *= -1
        else:
            precedence = _OPS_PRECEDENCE[c]
            while ops and precedence <= _OPS_PRECEDENCE[ops[-1]]:
                _apply_operator(ops.pop(), outputs)
            ops.append(c)

        i += 1

    while ops:
        _apply_operator(ops.pop(), outputs)

    if not outputs:
        raise ValueError("Expression resulted in empty stack")

    return outputs[-1]


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
    is_negative = False
    outputs = []

    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c.isdigit():
            num, i = _parse_num(expr, i)

            if is_negative:
                outputs[-1] = -num
                is_negative = False
            else:
                outputs.append(num)
        elif c == "_":
            is_negative = True
            outputs.append(0)
        else:
            _apply_operator(c, outputs)

        i += 1

    if not outputs:
        raise ValueError("Expression resulted in empty stack")

    return outputs[-1]
