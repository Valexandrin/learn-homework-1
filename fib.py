from functools import cache

@cache
def fib(number):
    """ fibonachi
    
    0, 1, 1, 2, 3, 5, 8
    """
    if number < 0:
        raise ValueError('число должно быть больше или равно нулю') 

    if number in (0, 1):
        return number        
    
    return fib(number - 1) + fib(number - 2)

print(fib(150))

