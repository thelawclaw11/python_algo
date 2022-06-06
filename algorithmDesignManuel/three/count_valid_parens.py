def count_valid_parens(s):
    result = 0
    stack = []

    for char in s:
        if char == ")":
            if stack:
                stack.pop()
                result += 2
        else:
            stack.append("(")
    return result


print(count_valid_parens(")()(())()()))())))("))