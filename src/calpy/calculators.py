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
        i += 1
    return stack[-1]
