from unittest import TestCase
from sessions.session06_functions.assignment05 import *


class Tester06Functions5(TestCase):

    def testExtreme(self):
        self.assertEqual(-7, extreme([-2, 1, 0, -3, -7]))
        self.assertEqual(7, extreme([1, 7, 0, -3, -7], False))

    def testScaleToPositive(self):
        array = [-2, 1, 0, -3, -7]
        self.assertEqual([5, 8, 7, 4, 0], shift_values_to_positive(array))
        self.assertEqual([-2, 1, 0, -3, -7], array)
        self.assertEqual([1, 2, 3, 4], shift_values_to_positive([1, 2, 3, 4]))

    def testSumAndDistribution(self):
        array = [-2, -1, 0, 1, 2]
        self.assertEqual(0, sum_of_values(array))
        self.assertEqual([0.0, 0.1, 0.2, 0.3, 0.4], distribution(array))
        self.assertEqual([-2, -1, 0, 1, 2], array)
        self.assertEqual([0.25, 0.25, 0.25, 0.25], distribution([3, 3, 3, 3]))

    def testHistogram(self):
        array = [-0.05, -0.05, -0.01, 0, 0.02, 0.01, 0.01, 0.01, -0.05]
        self.assertEqual([3, 0, 0, 0, 1, 1, 3, 1], histogram(array, 2))
        self.assertEqual([-0.05, -0.05, -0.01, 0, 0.02, 0.01, 0.01, 0.01, -0.05], array)

    def testSortThis(self):
        array = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        sort(array)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], array)

    def testGimmeSortedCopyOf(self):
        array = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        hard_copy = [9, 1, 5, 7, 3, 8, 4, 6, 2, 0]
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], sort_copy(array))
        self.assertEqual(hard_copy, array)
        self.assertEqual([-10, 0, 100], sort_copy([100, -10, 0]))