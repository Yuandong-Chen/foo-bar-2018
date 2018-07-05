def xor_to_n(n):
    if n <= 0:
        return 0
    dispatch = (n - 1) % 4
    if dispatch == 0:
        return 1
    elif dispatch == 1:
        return n + 1
    elif dispatch == 2:
        return 0
    else:
        return n

def answer(start, length):
    result = 0
    for lookover in range(length):
        result ^= xor_to_n(start + 0 + lookover * length - 1) ^ xor_to_n(start + length - 1 + lookover * (length - 1) )
    return result
