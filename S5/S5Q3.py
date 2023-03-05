n = int(input())

def rec(n):
    
    if n == 0:
        return    
    i = int(input())
    rec(n-1)
    print(i, end = ' ')

rec(n)

print()

from random import randrange

def func(n):
    if n == 0:
        return '–>'

    print(var := randrange(n), end=' ')
    return f'{func(n - 1)} {var}'


print(func(5))