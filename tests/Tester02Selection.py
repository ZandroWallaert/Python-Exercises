from tests.IOTestCase import IOTestCase
import math


class Tester02Selection(IOTestCase):

    def package_name(self):
        return "sessions.session02_selection"

    def test01_check_sign(self):
        self.assertOutputEqual("assignment01_check_sign", [1], "+\n")
        self.assertOutputEqual("assignment01_check_sign", [0], "+\n")
        self.assertOutputEqual("assignment01_check_sign", [-1], "-\n")
        self.assertOutputEqual("assignment01_check_sign", [100], "+\n")
        self.assertOutputEqual("assignment01_check_sign", [-100], "-\n")
    
    def test02_check_sign2(self):
        self.assertOutputEqual("assignment02_check_sign2", [1], "+\n")
        self.assertOutputEqual("assignment02_check_sign2", [0], "0\n")
        self.assertOutputEqual("assignment02_check_sign2", [-1], "-\n")
        self.assertOutputEqual("assignment02_check_sign2", [100], "+\n")
        self.assertOutputEqual("assignment02_check_sign2", [-100], "-\n")
    
    def test03_circle_surface2(self):
        self.assertOutputEqual("assignment03_circle_surface2", [10.5], str(10.5*10.5*math.pi)+"\n")
        self.assertOutputEqual("assignment03_circle_surface2", [-1], "?\n")

    def test04_odd(self):
        self.assertOutputEqual("assignment04_odd", [3], "odd\n")
        self.assertOutputEqual("assignment04_odd", [2], "even\n")
        self.assertOutputEqual("assignment04_odd", [1], "odd\n")
        self.assertOutputEqual("assignment04_odd", [0], "even\n")

        self.assertOutputEqual("assignment04_odd", [-3], "odd\n")
        self.assertOutputEqual("assignment04_odd", [-2], "even\n")
        self.assertOutputEqual("assignment04_odd", [-1], "odd\n")

        self.assertOutputEqual("assignment04_odd", [123], "odd\n")
        self.assertOutputEqual("assignment04_odd", [-123], "odd\n")
        self.assertOutputEqual("assignment04_odd", [246], "even\n")
        self.assertOutputEqual("assignment04_odd", [-246], "even\n")
    
    def test05_floating_point(self):
        self.assertOutputEqual("assignment05_floating_point", [0.5,-0.2], "equal\n")
        self.assertOutputEqual("assignment05_floating_point", [0.3,0.0], "equal\n")
        self.assertOutputEqual("assignment05_floating_point", [0.3,-0.0], "equal\n")
        self.assertOutputEqual("assignment05_floating_point", [0.4,0.2], "not equal\n")

    def test06_digit_swap(self):
        self.assertOutputEqual("assignment06_digit_swap", [1234], "1234\n")
        self.assertOutputEqual("assignment06_digit_swap", [-1234], "-1234\n")

        self.assertOutputEqual("assignment06_digit_swap", [-4], "-4\n")
        self.assertOutputEqual("assignment06_digit_swap", [4], "4\n")

        self.assertOutputEqual("assignment06_digit_swap", [34], "43\n")
        self.assertOutputEqual("assignment06_digit_swap", [-34], "-43\n")

        self.assertOutputEqual("assignment06_digit_swap", [70], "07\n")
        self.assertOutputEqual("assignment06_digit_swap", [-70], "-07\n")
    
    