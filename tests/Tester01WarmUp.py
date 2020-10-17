from tests.IOTestCase import IOTestCase
import math


class Tester01WarmUp(IOTestCase):

    def package_name(self):
        return "sessions.session01_warm_up"

    def test01_hello_world(self):
        self.assertOutputEqual("assignment01_hello_world", [], "Hello, World!\n")

    def test02_echo(self):
        self.assertOutputEqual("assignment02_echo", [123], "123\n")
        self.assertOutputEqual("assignment02_echo", ["azerty"], "azerty\n")
        self.assertOutputEqual("assignment02_echo", [1.4], "1.4\n")

    def test03_3x4_stars(self):
        self.assertOutputEqual("assignment03_3x4_stars", [], "****\n****\n****\n")

    def test04_swap(self):
        self.assertOutputEqual("assignment04_swap", [1,2], "2 1\n")

    def test05_swap2(self):
        self.assertOutputEqual("assignment05_swap2", [1,2], "2 1\n")
        self.assertOutputEqual("assignment05_swap2", [-1,-2], "-2 -1\n")
        self.assertOutputEqual("assignment05_swap2", [1,-2], "-2 1\n")
        self.assertOutputEqual("assignment05_swap2", [-1,2], "2 -1\n")

    def test06_circle_surface(self):
        self.assertOutputEqual("assignment06_circle_surface", [10.05], str(10.05*10.05*math.pi)+"\n")

    def test07_reverse_sequence(self):
        self.assertOutputEqual("assignment07_reverse_sequence", [1,2,3,4,5], "5\n4\n3\n2\n1\n")
