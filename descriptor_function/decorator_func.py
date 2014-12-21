'''
    - returns a decorator that can be used to decorate another function
    - verifies argument of the function it decorates <= the given value
    - raises a ValueError on failure.

    Example...

    >>> @minimum_x(6)
    ... def test(arg):
    ...   print arg
    ...

    >>> test(6)
    6

    >>> test(5) # raises ValueError
    '''


def minimum_x(x):
    def wrap(f):
        def wrapped_f(*args, **kwargs):
            if args[0] < x:
                raise ValueError
            f(*args, **kwargs)
        return wrapped_f
    return wrap


@minimum_x(6)
def test(arg):
    print arg
test(6)
test(5)
