def postfix(expr):
    stack = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            stack.append(int(expr[i:j]))
            i = j
        elif expr[i] == "+":
            stack.append(stack.pop() + stack.pop())
        elif expr[i] == " ":
            continue
        else:
            raise ValueError("Expression contains unsupported character")
        i += 1
    return stack[-1]
