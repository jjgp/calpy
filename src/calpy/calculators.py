def postfix(expr):
    i = 0
    stack = []
    supported_operators = {"+": lambda x, y: x + y}

    while i < len(expr):
        c = expr[i]

        if c.isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            stack.append(int(expr[i:j]))
            i = j
        elif c in supported_operators:
            if len(stack) < 2:
                raise ValueError("Expression resulted in empty stack")
            y, x = stack.pop(), stack.pop()
            result = supported_operators[c](x, y)
            stack.append(result)
        elif c == " ":
            pass
        else:
            raise ValueError("Expression contains unsupported character")
        i += 1

    if not stack:
        raise ValueError("Expression resulted in empty stack")

    return stack[-1]
