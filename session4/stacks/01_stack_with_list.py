# A stack with a plain list: the end of the list is the top
stack = []
stack.append("a")    # push
stack.append("b")
stack.append("c")
print(stack.pop())   # pop
print(stack[-1])     # peek
print(len(stack) == 0)  # is_empty
