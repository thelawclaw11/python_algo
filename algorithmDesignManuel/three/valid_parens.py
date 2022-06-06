def is_balanced(s):
    stack = []

    for char in s:
        if char == ")" and stack:
            stack.pop()
        else:
            stack.append(char)
    return not stack



print(is_balanced("((())())()"))
print(is_balanced(")()("))
print(is_balanced("())"))

