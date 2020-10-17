"""
Write the functions ```line```, ```rectangle```, ```parallelogram```, and ```triangle``` such that all tests succeed.

If the functionality you need already exists in (a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.

The focus in this exercise is to work with default parameters.
"""

def repeat(char, length):
    res = ''
    for i in range(length):
        res += char
    return res

def line(length, fill = True, indentation = 0,  char = '*'):
    fillChar = ' '
    if fill: fillChar = char
    res = repeat(' ', indentation)
    if length > 0: res += char
    res += repeat(fillChar, length - 2)
    if length > 1: res += char
    return res

def square(size, fill = True, indentation = 0,  char = '*'):
    return rectangle(size, size, fill, indentation, char)

def rectangle(width, height, fill = True, indentation = 0,  char = '*'):
    return parallelogram(width, height, fill, indentation, char, 0)

def parallelogram(width, height, fill = True, indentation = 0,  char = '*', step = -1):
    indentSurplus = 0
    if step < 0: indentSurplus = -step * (height-1)
    res = line(width, True, indentation + indentSurplus, char)
    indentSurplus += step
    for r in range(height - 2):
        res += '\r\n' + line(width, fill, indentation + indentSurplus, char)
        indentSurplus += step
    if height > 1: res += '\r\n' + line(width, True, indentation + indentSurplus, char)
    return res

def triangle(width, fill = True, indentation = 0,  char = '*', step = 0, alignRight = False, fromTopToBottom = True, rightAngled = True):
    res = ''
    spacesPerLine = 0
    spacesIncrement = 0 + step
    charsPerLine = 1
    charsIncrement = +1
    if not fromTopToBottom:
        charsPerLine = width
        charsIncrement = -1
    else:
        if alignRight:
            spacesPerLine = width - 1
            spacesIncrement = -step

    if not rightAngled:
        if not fromTopToBottom: charsPerLine = width
        width //= 2
        if width % 2 == 1: width += 1
        else:
            if fromTopToBottom: charsPerLine = 2
        spacesPerLine = width - 1
        charsIncrement = 2
        spacesIncrement = -1 - step
        if not fromTopToBottom:
            spacesPerLine = 0
            spacesIncrement = +1 + step
            charsIncrement = -2

    for i in range(width):
        if i == width - 1 or i == 0: lineFill = True
        else: lineFill = fill
        res += line(charsPerLine, lineFill, indentation + spacesPerLine,  char)
        if i < width - 1: res += '\r\n'
        spacesPerLine += spacesIncrement
        charsPerLine += charsIncrement
    return res

