
from functools import lru_cache
def fib(n):
    if n >= 0:
        if n in [0, 1]:
            return n
        else:
            return fib(n - 2) + fib(n - 1)

@lru_cache(None)
def fibIter(n):
    prev, current = 0, 1
    next = 0
    for i in range(n):
        next = prev + current
        prev, current = current, next
    return prev

# print((fibIter(1000000)))

def negafibIter(n):
    prev, curent = 0, 1
    next = 0
    for i in range(abs(n)):
        next = prev - curent
        prev,curent = curent,next
    return prev

print(negafibIter(-1000000))

