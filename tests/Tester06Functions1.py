from unittest import TestCase
from sessions.session06_functions.assignment01 import *
import math

class Tester06Functions1(TestCase):

    def assertIsNaN(self, n):
        self.assertTrue(math.isnan(n))

    def testGcd(self):
        self.assertNotEqual(math.gcd, gcd)
        self.assertEqual(13, gcd(273, 1430))
        self.assertEqual(3, gcd(15, 12))

    def testSwap(self):
        self.assertEqual(-43021, swap_digits(-1203400))

    def testFac(self):
        self.assertEqual(5040, factorial(7))
        self.assertEqual(1, factorial(0))

    def testAvg(self):
        self.assertAlmostEqual(1.5, avg([0, 1, 2, 3]))
        self.assertAlmostEqual(0, avg([-3, -1, 1, 3, 0]))
        self.assertIsNaN(avg([]))

    def testLargestPrime(self):
        self.assertEqual(101, largest_prime(102))
        self.assertEqual(101, largest_prime(101))
        self.assertEqual(97, largest_prime(100))
        self.assertEqual(2, largest_prime(2))
        self.assertIsNaN(largest_prime(1))
        self.assertIsNaN(largest_prime(0))
        self.assertIsNaN(largest_prime(-1))

    def testVariation(self):
        self.assertEqual(7, variation(7, 1))
        self.assertEqual(5040, variation(7, 6))
        self.assertEqual(1500000000, variation(1500000000, 1))
        self.assertEqual(0, variation(6, 7))
        self.assertEqual(0, variation(-7, -6))
        self.assertEqual(0, variation(-7, 6))
        self.assertEqual(0, variation(7, -6))
        self.assertEqual(1, variation(0, 0))