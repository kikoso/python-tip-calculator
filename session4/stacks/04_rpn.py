# Exercise: evaluate reverse Polish notation (UPN) with a stack


def eval_rpn(expr):
    stack = []
    for token in expr.split():
        if token in ("+", "-", "*", "/"):
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            else:
                stack.append(a / b)
        else:
            stack.append(float(token))
    return stack.pop()


print(eval_rpn("3 4 + 2 *"))
print(eval_rpn("10 2 8 * + 3 -"))
print(eval_rpn("8 2 /"))
