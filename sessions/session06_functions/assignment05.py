"""
Implement the functions ```extreme```, ```shift_values_to_positive```, ```distribution```, ```histogram```,
```sort```, and ```sort_copy``` such that all tests succeed.

If the functionality you need already exists in (a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""

def extreme(array, min = True):
    minValue = array[0]
    maxValue = array[0]
    for i in range(1, len(array)):
        if array[i] < minValue: minValue = array[i]
        if array[i] > maxValue: maxValue = array[i]
    if min: return minValue
    else: return maxValue

def shift_values_to_positive(array):
    res = [0] * len(array)
    min = extreme(array)
    if min > 0: min = 0
    for i in range(len(array)):
        res[i] = array[i] - min
    return res

def sum_of_values(array):
    sum = 0.0
    for i in range(len(array)):
        sum += array[i]
    return sum

def distribution(array):
    res = shift_values_to_positive(array)
    sum = sum_of_values(res)
    for i in range(len(array)):
        res[i] /= sum
    return res

def histogram(array, precision):
    scaled = shift_values_to_positive(array)
    frequencyOf = [0] * (1 + int(extreme(scaled, False) * (10 ** precision)))
    for i in range(len(scaled)):
        frequencyOf[int(scaled[i] * (10 ** precision))] += 1
    return frequencyOf

def copyOf(array):
    copy = []
    for value in array:
        copy.append(value)
    return copy

def sort(array):
    for i in range(len(array)-1):
        minAt = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minAt]:
                minAt = j
        tmp = array[minAt]
        array[minAt] = array[i]
        array[i] = tmp

def sort_copy(array):
    res = copyOf(array)
    sort(res)
    return res

