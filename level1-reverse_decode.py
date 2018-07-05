def answer(s):
    def convert(ch):
        ch = ord(ch)
        if ch>= 97 and ch <= 122:
            return 122 - (ch - 97)
        else:
            return ch
    L = map(convert, list(s))
    return ''.join(chr(i) for i in L)
