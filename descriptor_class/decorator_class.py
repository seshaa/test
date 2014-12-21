class minimum_x(object):
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
    def __init__(self, arg):
        '''
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        '''
        self.arg = arg

    def __call__(self, f):
        '''
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        '''
        def wrapped_f(*args, **kwargs):
            if (args[0] < self.arg):
                raise ValueError
            f(*args, **kwargs)
        return wrapped_f

if (__name__ == '__main__'):
    @minimum_x(6)
    def test(arg):
        print arg

    test(6)
    test(5)
