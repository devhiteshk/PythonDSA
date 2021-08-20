def rM(n):
    if n < 1:
        print("n is less than 1")
    else:
        rM(n - 1)
        print(n)


rM(10)  # How STACK MEMORY WORKS Last in First Out


# Factorial by recursion

def factorial(n):
    assert 0 <= n and int(n) == n, "The number must be positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(10))


# Fibonacci by Recursion

def Fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only"
    if n in [0, 1]:
        return n
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(Fibonacci(6))


# Interview questions
# How to find sum of digits by recursion


def sumofDigits(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer"
    if n == 0:
        return 0
    else:
        return int(n % 10) + sumofDigits(int(n / 10))


print(sumofDigits(11))


# How to calculate Power of a number by Recursion
def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "Error: The exponent cannot be positive integer"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * power(base, exp - 1)


print(power(2, 2))


# Greatest common divisor by recursion

def gcd(a, b):
    assert int(a) == a and int(b) == b, "The number must be integer only"
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(48, -18))


# How to convert a number from decimal to binary
def decimaltoBin(n):
    assert int(n) == n, "The parameter must be an integer"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimaltoBin(int(n / 2))


print(decimaltoBin(100))


