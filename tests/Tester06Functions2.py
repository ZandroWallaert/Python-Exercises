from unittest import TestCase
from sessions.session06_functions.assignment02 import *


class Tester06Functions2(TestCase):

    def testSplit(self):
        self.assertEqual(['appels', 'en', 'peren'], split('appels en peren', ' '))
        self.assertEqual(['appels', 'en', 'peren'], split(' appels en peren ', ' '))
        self.assertEqual(['appels', 'peren'], split(' appels & peren&', '&'))
        self.assertEqual(['appels', 'peren'], split('& &appels & peren& ', '&'))
        self.assertEqual(['appels en peren'], split('& &appels en peren& &', '&'))
        self.assertEqual(['appels en peren', 'bananen'], split('& &appels en peren& bananen&', '&'))

    def testIsDigit(self):
        self.assertTrue(is_digit('9'))
        self.assertFalse(is_digit('a'))
        self.assertFalse(is_digit('A'))
        self.assertFalse(is_digit('@'))

    def testToUpper(self):
        self.assertEqual('123ABCXYZ#@&', to_upper('123abcXYZ#@&'))

    def testToLower(self):
        self.assertEqual('123abcxyz#@&', to_lower('123abcXYZ#@&'))

    def testIsAlpha(self):
        self.assertTrue(is_alpha('a'))
        self.assertTrue(is_alpha('A'))
        self.assertFalse(is_alpha('9'))
        self.assertFalse(is_alpha('%'))

    def testIsInt(self):
        self.assertTrue(is_int('314'))
        self.assertTrue(is_int('-314'))
        self.assertFalse(is_int('-3.14'))
        self.assertTrue(is_int('+  314'))
        self.assertFalse(is_int('@  314'))

    def testTrim(self):
        self.assertEqual('abc', trim(' \t\r\nabc \t\r\n'))
        self.assertEqual('a', trim(' \t\r\na \t\r\n'))
        self.assertEqual('', trim(' \t\r\n \t\r\n'))
        self.assertEqual('a\rb', trim(' \t\ra\rb \t\r\n'))
