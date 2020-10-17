"""
Implements the functions ```is_leap_year```, ```number_of_days_in_month```, ```number_of_days_in_year```,
```number_of_day_in_year```, ```date_diff_in_days```, ```compare```, ```date```, ```add_days_to_date```,
```birthday_already_passed```, and ```age```, such that all tests succeed. Tuples can be used in return-types,
not in parameters (see the tests).

If the functionality you need already exists in (a) Python (library), try to implement it yourself.
The exercise here is to write code, not to borrow it.
"""
from datetime import *

def today():  # given
    now = datetime.today()
    return now.year, now.month, now.day

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def number_of_days_in_month(year, month = 0):
    number_of_days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year): number_of_days_in_month[2] = 29
    if month != 0: return number_of_days_in_month[month]
    else: return 337 + number_of_days_in_month[2]

def number_of_day_in_year(year, month, day, sinceYear = -1):
    number_of_days_in_year = day
    for m in range(1, month):
        number_of_days_in_year += number_of_days_in_month(year, m)
    if sinceYear != -1:
        for y in range(sinceYear, year):
            number_of_days_in_year += number_of_days_in_month(y)
    return number_of_days_in_year

def date(days, sinceYear):
    if days >= 0:
        year = sinceYear
        month = 1
        diff = 1
    else:
        year = sinceYear - 1
        month = 12
        diff = -1
        days = -days
    while days > number_of_days_in_month(year):
        days -= number_of_days_in_month(year)
        year += diff
    while days > number_of_days_in_month(year, month):
        days -= number_of_days_in_month(year, month)
        month += diff
    if diff == -1:
        days = number_of_days_in_month(year, month) - days + 1
    return year, month, days

def add_days_to_date(year, month, day, days):
    serialDays = number_of_day_in_year(year, month, day, year) + days
    if serialDays <= 0:
        serialDays -= 1
    return date(serialDays, year)

def before(aYear, aMonth, aDay, anotherYear, anotherMonth, anotherDay):
    res = date_diff_in_days(aYear, aMonth, aDay, anotherYear, anotherMonth, anotherDay)
    if res != 0: res = res / abs(res)
    return res

def compare(aYear, aMonth, aDay, anotherYear, anotherMonth, anotherDay):
    return -before(aYear, aMonth, aDay, anotherYear, anotherMonth, anotherDay)

def date_diff_in_days(fromYear, fromMonth,  fromDay, toYear, toMonth, toDay):
    since = min(fromYear, toYear)
    return number_of_day_in_year(toYear, toMonth, toDay, since) - number_of_day_in_year(fromYear, fromMonth, fromDay, since)

def birthday_already_passed(bornInYear, bornInMonth, bornOnDay):
    thisYear, thisMonth,thisDay = today()
    if thisYear < bornInYear: return False
    if before(thisYear, bornInMonth, bornOnDay, thisYear, thisMonth, thisDay) > 0:
        return True
    else:
        return False

def age(bornInYear, bornInMonth, bornOnDay):
    thisYear, thisMonth, thisDay = today()
    currAge = thisYear - bornInYear
    if not birthday_already_passed(bornInYear, bornInMonth, bornOnDay):
        currAge -= 1
    if currAge < 0: currAge = 0
    return currAge

