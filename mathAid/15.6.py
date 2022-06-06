coins = [4, 10, 15]

def can_make_change(target):
    if target == 0:
        return True
    if target < 0:
        return False

    result = False

    for c in coins:
        result = can_make_change(target - c)
        if result:
            result = True
            break

    return result


print(can_make_change(10))

for n in range(0, 100):
    print(n, "-->",can_make_change(n))





