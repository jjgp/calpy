import math


def infix(_):
    raise NotImplementedError("Infix notation is not yet supported")


def postfix(expr):
    """
    Implements to evaluation of an mathematical expression by Reverse Polish notation.

    For more:
        https://en.wikipedia.org/wiki/Reverse_Polish_notation

    :param expr: a string representing the expression to be evaluated
    :returns: the resulting integer value
    :raises ValueError: expressions resulting in empty stacks, for divison or
    remainder by zero, and unsupported characters
    """

    i = 0
    stack = []
    supported_operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: int(x / y),
        "%": math.fmod,
    }

    while i < len(expr):
        c = expr[i]

        if c == " ":
            pass
        elif c.isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            stack.append(int(expr[i:j]))
            i = j
        elif c in supported_operators:
            if len(stack) < 2:
                raise ValueError("Expression resulted in empty stack")
            if c == "/" and stack[-1] == 0:
                raise ValueError("Expression resulted in division by zero")
            if c == "%" and stack[-1] == 0:
                raise ValueError("Expression resulted in remainder by zero")

            y, x = stack.pop(), stack.pop()
            result = supported_operators[c](x, y)
            stack.append(result)
        else:
            raise ValueError("Expression contains unsupported character")

        i += 1

    if not stack:
        raise ValueError("Expression resulted in empty stack")

    return stack[-1]
