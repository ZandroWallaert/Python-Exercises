"""
Write the functions ```sub_str```, ```reverse```, ```is_palindrome```, ```find```, ```find_all```,
 and ```to_dutch```, such that all tests succeed.

The key of this exercise is to start small: make your function work for simple and small input.
E.G., make your to_dutch function first for digits, than for 2digit numbers, etc. Just like in the previous exercise
the key is to reuse existing functions.

If the functionality you need already exists in (a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""

words = ['nul', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes', 'zeven', 'acht', 'negen',
         'tien', 'elf', 'twaalf', 'dertien', 'veertien', 'vijftien', 'zestien', 'zeventien', 'achttien', 'negentien']
multiples = ['nul', 'tien', 'twintig', 'dertig', 'veertig', 'vijftig', 'zestig', 'zeventig', 'tachtig', 'negentig']
numerals = ['', 'duizend ', ' miljoen ', ' miljard ', ' biljoen ', ' biljard ', ' triljoen ', ' triljard ']

def sub_str(s, start, length):
    res = ''
    start = clip(0, start, len(s))
    if length < 0:
        to = start
        start += length
    else:
        to = start + length
    start = clip(0, start, len(s))
    to = clip(0, to, len(s))
    i = start
    while i < to:
        res += s[i]
        i += 1
    return res

def reverse(s):
    res = ''
    for i in range (len(s)):
        res = s[i] + res
    return res

def is_palindrome(s):
    if len(s) == 0: return False
    return s == reverse(s)

def decompose(number):
    strnum = str(number)
    digits = [0] * len(strnum)
    for i in range(len(strnum)):
        digits[len(strnum) - 1 - i] = int(strnum[i])
    return digits

def to_dutch_3digits(number, multiple = ''):
    if number < 0 or 999 < number: return ''
    ones = number % 10
    tens = (number // 10) % 10
    hundreds = (number // 100) % 10
    res = ''
    if hundreds >= 1:
        if hundreds > 1:
            res += words[hundreds]
        res += 'honderd'
    if tens <= 1:
        if res != '' and ones > 0 and tens < 1: res += 'en'
        if number % 100 != 0 or number == 0: res += words[tens * 10 + ones]
    else:
        word = words[ones]
        if word[len(word) - 1] == 'e':
            res += words[ones] + 'ën' + multiples[tens]
        else:
            res += words[ones] + 'en' + multiples[tens]
    return res

def to_dutch(number):
    i = 0
    res = ''
    while number > 0:
        res = to_dutch_3digits(number % 1000) + numerals[i] + res
        number //= 1000
        i += 1
    return res

def replace(hit, replacement, haystack):
    hits = find_all(hit, haystack)
    res = ''
    pos = 0
    for i in hits:
        if i > pos: res += sub_str(haystack, pos, i - pos)
        res += replacement
        pos = i + len(hit)
    res += sub_str(haystack, pos, len(haystack) - pos)
    return res

def clip(min, value, max):
    if -max < value and value < 0: value = max + value
    if value < min: return min
    if value > max: return max
    return value



def find(needle, haystack, start = 0):
    while start + len(needle) <= len(haystack):
        if sub_str(haystack, start, len(needle)) == needle: return start
        start += 1
    return -1

def find_all(needle, haystack, start = 0):
    res = []
    pos = find(needle, haystack, start)
    while pos != -1:
        res.append(pos)
        start += pos + 1
        pos = find(needle, haystack, start)
    return res