from unittest import TestCase
from sessions.session06_functions.assignment04 import *


class Tester06Functions4(TestCase):

    def testIsLeapYear(self):
        self.assertTrue(is_leap_year(2016))
        self.assertFalse(is_leap_year(1997))
        self.assertTrue(is_leap_year(1996))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2000))

    def testNumberOfDaysIn(self):
        self.assertEqual(28, number_of_days_in_month(2017, 2))
        self.assertEqual(29, number_of_days_in_month(2016, 2))
        self.assertEqual(31, number_of_days_in_month(1996, 7))
        self.assertEqual(365, number_of_day_in_year(1997))
        self.assertEqual(366, number_of_days_in_year(1996))

    def testNumberOfDay(self):
        self.assertEqual(365, number_of_day_in_year(2017, 12, 31))
        self.assertEqual(366, number_of_day_in_year(2016, 12, 31))
        self.assertEqual(1, number_of_day_in_year(2016, 1, 1))

    def testDateDiffInDays(self):
        self.assertEqual(0, date_diff_in_days(2017, 1, 1, 2017, 1, 1))
        self.assertEqual(1, date_diff_in_days(2017, 1, 1, 2017, 1, 2))
        self.assertEqual(-90, date_diff_in_days(2016, 3, 31, 2016, 1, 1))
        self.assertEqual(90, date_diff_in_days(2016, 1, 1, 2016, 3, 31))
        self.assertEqual(730, date_diff_in_days(2015, 4, 1, 2017, 3, 31))
        self.assertEqual(-730, date_diff_in_days(2017, 3, 31, 2015, 4, 1))

    def testCompare(self):
        self.assertTrue(compare(2016, 2, 29, 2016, 3, 31) < 0)
        self.assertTrue(compare(2017, 3, 31, 2015, 4, 1) > 0)
        self.assertEqual(0, compare(2017, 3, 31, 2017, 3, 31))

    def testDate(self):
        self.assertEqual((1901, 2, 14), date(365 + 31 + 14, 1900))
        self.assertEqual((2016, 12, 31), date(-1, 2017))
        self.assertEqual((2015, 3, 19), date(-654, 2017))

    def testAddDaysToDate(self):
        self.assertEqual((1902, 2, 14), add_days_to_date(1901, 1, 1, 365 + 31 + 13))
        self.assertEqual((2004, 11, 30), add_days_to_date(1999, 2, 1, 2129))
        self.assertEqual((1999, 2, 1), add_days_to_date(2004, 11, 30, -2129))
        self.assertEqual((1901, 1, 2), add_days_to_date(1900, 12, 30, 3))
        self.assertEqual((1900, 12, 30), add_days_to_date(1901, 1, 2, -3))
        self.assertEqual((2015, 3, 19), add_days_to_date(2017, 1, 1, -654))

    def testBirthdayAlreadyPassedThisYear(self):
        self.assertTrue(birthday_already_passed(1971, 1, 1))  # test will fail at "nieuwjaarsdag".
        self.assertFalse(birthday_already_passed(1971, 12, 31))
        self.assertFalse(birthday_already_passed(2100, 1, 1))

    def testAge(self):
        current_year, _, _ = today()
        self.assertEqual(0, age(2100, 1, 1))
        self.assertEqual(10, age(current_year - 10, 1, 1))
        self.assertEqual(9, age(current_year - 10, 12, 31))  # test will fail at "oudejaarsavond".
