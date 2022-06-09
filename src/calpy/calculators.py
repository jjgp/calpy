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


def _operate_on_stack(op, stack):
    if op not in _OPS_SUPPORTED:
        raise ValueError("Expression contains unsupported character")
    elif len(stack) < 2:
        raise ValueError("Expression resulted in empty stack")
    elif op == "/" and stack[-1] == 0:
        raise ValueError("Expression resulted in division by zero")
    elif op == "%" and stack[-1] == 0:
        raise ValueError("Expression resulted in remainder by zero")

    y, x = stack.pop(), stack.pop()
    result = _OPS_SUPPORTED[op](x, y)
    stack.append(result)


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
    stack = []

    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c == "(":
            ops.append(c)
        elif c.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = 10 * num + int(expr[i])
                i += 1
            i -= 1

            stack.append(num)
        elif c == ")":
            while ops and ops[-1] != "(":
                _operate_on_stack(ops.pop(), stack)
            ops.pop()
        else:
            precedence = _OPS_PRECEDENCE[c]
            while ops and (_OPS_PRECEDENCE[ops[-1]] >= precedence):
                _operate_on_stack(ops.pop(), stack)
            ops.append(c)

        i += 1

    while ops:
        _operate_on_stack(ops.pop(), stack)

    if not stack:
        raise ValueError("Expression resulted in empty stack")

    return stack[-1]


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
    stack = []

    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c == "_":
            is_negative = True
            stack.append(0)
        elif c.isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = 10 * num + int(expr[i])
                i += 1
            i -= 1

            if is_negative:
                stack[-1] = -num
                is_negative = False
            else:
                stack.append(num)
        else:
            _operate_on_stack(c, stack)

        i += 1

    if not stack:
        raise ValueError("Expression resulted in empty stack")

    return stack[-1]
