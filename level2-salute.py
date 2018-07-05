def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        try:
            initializer = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    accum_value = initializer
    for x in it:
        accum_value = function(accum_value, x)
    return accum_value

def answer(s):
    def func(state, ele):
        accum, count = state
        if ele == '>':
            accum += 1
        elif ele == '<':
            count += accum * 2
        return (accum, count)
    _, result = reduce(func, s, (0, 0))
    return result
