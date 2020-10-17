from tests.IOTestCase import IOTestCase


class Tester03Iteration(IOTestCase):

    def package_name(self):
        return "sessions.session03_iteration"

    def test01_sentinel(self):
        self.assertOutputEqual("assignment01_sentinel", [1,-2,3,-4,0], "4\n")

    def test02_average(self):
        res = float(self.get_output("assignment02_average", [1.4, -2.1, 3.0, -4, 0]))
        self.assertAlmostEqual(res, -0.425)

        self.assertOutputEqual("assignment02_average", [0], "no data\n")

    def test03_factorial(self):
        self.assertOutputEqual("assignment03_factorial", [5], "120\n")
        self.assertOutputEqual("assignment03_factorial", [1], "1\n")
        self.assertOutputEqual("assignment03_factorial", [0], "1\n")
        self.assertOutputEqual("assignment03_factorial", [-1], "1\n")
        self.assertOutputEqual("assignment03_factorial", [-5], "1\n")

    def test04_star_square(self):
        self.assertOutputEqual("assignment04_star_square", [3,4], "****\n****\n****\n\n")
        self.assertOutputEqual("assignment04_star_square", [4,3], "***\n***\n***\n***\n\n")
        self.assertOutputEqual("assignment04_star_square", [4,0], "")
        self.assertOutputEqual("assignment04_star_square", [0,3], "")
        self.assertOutputEqual("assignment04_star_square", [0,0], "")

    def test05_isosceles1(self):
        self.assertOutputEqual("assignment05_isosceles1", [3], "*\n**\n***\n")
        self.assertOutputEqual("assignment05_isosceles1", [-1,-2,0,3], "*\n**\n***\n")

    def test06_isosceles2(self):
        self.assertOutputEqual("assignment06_isosceles2", [3], "***\n**\n*\n")
        self.assertOutputEqual("assignment06_isosceles2", [-1, -2, 0, 3], "***\n**\n*\n")

    def test07_isosceles3(self):
        self.assertOutputEqual("assignment07_isosceles3", [3], "***\n **\n  *\n")
        self.assertOutputEqual("assignment07_isosceles3", [-1, -2, 0, 3], "***\n **\n  *\n")

    def test08_isosceles4(self):
        self.assertOutputEqual("assignment08_isosceles4", [3], "  *\n **\n***\n")
        self.assertOutputEqual("assignment08_isosceles4", [-1,-2,0,3], "  *\n **\n***\n")

    def test09_isosceles5(self):
        self.assertOutputEqual("assignment09_isosceles5", [5], "  *\n ***\n*****\n")
        self.assertOutputEqual("assignment09_isosceles5", [-1, -2, 0, 5], "  *\n ***\n*****\n")

        self.assertOutputEqual("assignment09_isosceles5", [6], "  **\n ****\n******\n")
        self.assertOutputEqual("assignment09_isosceles5", [-1, -2, 0, 6], "  **\n ****\n******\n")

    def test10_isosceles6(self):
        self.assertOutputEqual("assignment10_isosceles6", [5], "*****\n ***\n  *\n")
        self.assertOutputEqual("assignment10_isosceles6", [-1, -2, 0, 5], "*****\n ***\n  *\n")

        self.assertOutputEqual("assignment10_isosceles6", [6], "******\n ****\n  **\n")
        self.assertOutputEqual("assignment10_isosceles6", [-1, -2, 0, 6], "******\n ****\n  **\n")

    def test11_euclid(self):
        self.assertOutputEqual("assignment11_euclid", [225,15], "15\n")
        self.assertOutputEqual("assignment11_euclid", [15,12], "3\n")

    def test12_digit_swap2(self):
        self.assertOutputEqual("assignment12_digit_swap2", [1234], "4321\n")
        self.assertOutputEqual("assignment12_digit_swap2", [-1234], "-4321\n")
        self.assertOutputEqual("assignment12_digit_swap2", [0], "0\n")
        self.assertOutputEqual("assignment12_digit_swap2", [6], "6\n")
        self.assertOutputEqual("assignment12_digit_swap2", [-6], "-6\n")
        self.assertOutputEqual("assignment12_digit_swap2", [700], "7\n")
        self.assertOutputEqual("assignment12_digit_swap2", [-700], "-7\n")
