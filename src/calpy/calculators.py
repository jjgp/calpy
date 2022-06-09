import math


def infix(_):
    raise NotImplementedError("Infix notation is not yet supported")


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
