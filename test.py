from functools import lru_cache

@lru_cache(None)

def fib(n):
        if n >= 0:
            prev, current = 0, 1
            next = 0
            for i in range(0, n):
                next = prev + current
                prev, current = current, next
            return prev

        if n <= 0:
            prev, current = 0, 1
            next = 0
            for i in range(0, abs(n)):
                next = prev - current
                prev, current = current, next
            return prev

print(fib(-10))