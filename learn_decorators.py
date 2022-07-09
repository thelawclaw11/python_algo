from functools import cache


def with_auto_cache(func):
    cache = {}

    def f(*args):
        key = hash(*args)

        if key in cache:
            return cache[key]

        cache[key] = func(*args)
        return cache[key]

    # func = f
    return f


@with_auto_cache
def fib(n):
    return 1 if n < 2 else fib(n - 1) + fib(n - 2)

def add1(x):
    return x + 1

def add2(x):
    return x + 2

fib = with_auto_cache(fib)

print(fib(10))

print(add1(1))
print(add2(1))

# print(with_auto_cache(fib)(30))

# print(fib(40))

# print(fib_with_cache(30))
#
# print(fib(30))
# print(fib(30))
