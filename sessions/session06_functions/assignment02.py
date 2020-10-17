"""
Write the functions ```split```, ```is_digit```, ```to_upper```, ```to_lower```, ```is_alpha```, ```is_int```, and
```trim```.
All these functions should be written such that the tests succeed. The goal of this exercise is to create a lot of
small helper functions and to re-use them. For example, maybe it is interesting to first implement ```trim````.
It can be (re-)used in many other functions. You can/should also create functions that are not in the list above...
For example the given function ```is_whitespace```.

If the functionality you need already exists in (a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.

You can make use of ```ord()``` and ```chr()``` that respectively turn a character into an integer, and vice versa.
Hence, it is not necessary to implement ```ord()``` and ```chr()``` yourself.
First play with these two functions until you understand how they work.

"""


def is_whitespace(ch):  # given
    return ch == ' ' or ch == '\t' or ch == '\r' or ch == '\n'

def trim(s):
    start = 0
    stop = len(s) - 1
    while start <= stop and is_whitespace(s[start]): start += 1
    while stop > start and is_whitespace(s[stop]): stop -= 1
    res = ''
    for i in range(start, stop + 1):
        res += s[i]
    return res

def split(s, sep):
    res = []
    word = ''
    s += sep

    for ch in s:
        if ch == sep:
            word = trim(word)
            if word != '':
                res.append(word)
                word = ''
        else:
            word += ch

    return res

def inRange(lower, ch, upper):
    return lower <= ch and ch <=  upper

def is_digit(ch):
    return inRange('0', ch, '9')

def isUpper(ch):
    return inRange('A', ch, 'Z')

def isLower(ch):
    return inRange('a', ch, 'z')

def to_upper(s):
    res = ''
    for ch in s:
        if isLower(ch):
            res += chr(ord(ch) - ord('a') + ord('A'))
        else:
            res += ch
    return res

def to_lower(s):
    res = ''
    for ch in s:
        if isUpper(ch):
            res += chr(ord(ch) + ord('a') - ord('A'))
        else:
            res += ch
    return res

def is_alpha(ch):
    return isUpper(ch) or isLower(ch)

def is_int(s):
    parts = split(s, ' ')
    s = ''
    for i in range(len(parts)):
        s += parts[i]
    start = 0
    if s[0] == '-' or s[0] == '+': start = 1
    for i in range(start, len(s)):
        if not is_digit(s[i]):
            return False
    return True

