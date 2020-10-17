from unittest import TestCase
from sessions.session06_functions.assignment03 import *


class Tester06Functions3(TestCase):

    def testSubStr(self):
        self.assertEqual('', sub_str('voetbalveld', 0, 0))
        self.assertEqual('', sub_str('voetbalveld', 0, -1))
        self.assertEqual('', sub_str('voetbalveld', -11, -1))
        self.assertEqual('', sub_str('voetbalveld', -15, -1))
        self.assertEqual('', sub_str('voetbalveld', 11, 1))
        self.assertEqual('voet', sub_str('voetbalveld', -11, 4))
        self.assertEqual('veld', sub_str('voetbalveld', 11, -4))
        self.assertEqual('voetbalveld', sub_str('voetbalveld', -11, 12))

        self.assertEqual('voet', sub_str('voetbalveld', 0, 4))
        self.assertEqual('bal' , sub_str('voetbalveld', 4, 3))
        self.assertEqual('bal', sub_str('voetbalveld', 7, -3))
        self.assertEqual('bal', sub_str('voetbalveld', -7, 3))
        self.assertEqual('bal', sub_str('voetbalveld', -4, -3))
        self.assertEqual('veld', sub_str('voetbalveld', 7, 4))

    def testReverse(self):
        self.assertEqual('', reverse(''))
        self.assertEqual('lab', reverse('bal'))

    def testIsPalindrome(self):
        self.assertFalse(is_palindrome(''))
        self.assertTrue(is_palindrome('aibohphobia'))
        self.assertFalse(is_palindrome('test'))

    def testFind(self):
        self.assertEqual(4, find('bal', 'voetbalbal'))
        self.assertEqual(4, find('bal', 'voetbalbal', 4))
        self.assertEqual(7, find('bal', 'voetbalbal', 5))
        self.assertEqual(0, find('haha', 'hahaha'))
        self.assertEqual(2, find('haha', 'hahaha', 1))
        self.assertEqual(-1, find('haha', 'hahaha', 3))
        self.assertEqual(-1, find('haha', 'ha'))

    def testFindAll(self):
        self.assertEqual([0, 2, 4],find_all('ha', 'hahaha'))
        self.assertEqual([0, 2], find_all('haha', 'hahaha'))
        # geen overlap -> self.assertEqual([0], findAll('haha', 'hahaha'))
        self.assertEqual([2, 4], find_all('ha', 'hahaha', 1))
        # geen overlap -> self.assertEqual([6], findAll('haha', 'hahahihahahahihiha', 1))
        self.assertEqual([6, 8], find_all('haha', 'hahahihahahahihiha', 1))
        # geen overlap -> self.assertEqual([0, 6], findAll('haha', 'hahahihahahahihiha'))
        self.assertEqual([0, 6, 8], find_all('haha', 'hahahihahahahihiha'))

    def testReplace(self):
        self.assertEqual('voetloblob', replace('bal', 'lob', 'voetbalbal'))
        self.assertEqual('voet', replace('bal', '', 'voetbalbal'))
        self.assertEqual('balbal', replace('voet', '', 'voetbalbal'))
        self.assertEqual('voetbalbal', replace('sok', 'lob', 'voetbalbal'))
        self.assertEqual('hohohoho', replace('haha', 'hoho', 'hahaha'))
        # geen overlap -> self.assertEqual('hohoha', replace('haha', 'hoho', 'hahaha'))'

    def testInDutch(self):
        self.assertEqual('nul', to_dutch_3digits(0))
        self.assertEqual('negen', to_dutch_3digits(9))
        self.assertEqual('achttien', to_dutch_3digits(18))
        self.assertEqual('zevenenvijftig', to_dutch_3digits(57))
        self.assertEqual('tweeëntwintig', to_dutch_3digits(22))
        self.assertEqual('honderdtien', to_dutch_3digits(110)) # !!!
        self.assertEqual('driehonderdvijftien', to_dutch_3digits(315))
        self.assertEqual('driehonderddrieëndertig', to_dutch_3digits(333))
        self.assertEqual('driehonderd', to_dutch_3digits(300))
        self.assertEqual('driehonderdenzeven', to_dutch_3digits(307))
        self.assertEqual('zevenhonderdeenentachtig miljoen vierhonderdtweeënvijftigduizend driehonderdeenentwintig',
                         to_dutch(781452321))

    def testDecompose(self):
        self.assertEqual([1, 0, 2, 0, 3], decompose(30201))
