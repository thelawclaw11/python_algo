def get_divisors(n):
    out = []
    for i in range(1, n + 1):
        if n % i == 0:
            out.append(i)
    return out

print(get_divisors(42))