from tests.IOTestCase import IOTestCase
from multiprocessing import Process


class Tester05AllRound(IOTestCase):

    def package_name(self):
        return "sessions.session05_allround"

    def test01_sentinel_extreme(self):
        self.assertOutputEqual("assignment01_sentinel_extreme", [0], "0 0\n")
        self.assertOutputEqual("assignment01_sentinel_extreme", [1,0], "1 1\n")
        self.assertOutputEqual("assignment01_sentinel_extreme", [-1,0], "-1 -1\n")
        self.assertOutputEqual("assignment01_sentinel_extreme", [-1, 1,0], "-1 1\n")
        self.assertOutputEqual("assignment01_sentinel_extreme", [1, 2,0], "1 2\n")
        self.assertOutputEqual("assignment01_sentinel_extreme", [-1, -2,0], "-2 -1\n")

    def test02_faculteit2(self):
        self.assertOutputEqual("assignment02_faculteit2", [-1], "undefined\n")
        self.assertOutputEqual("assignment02_faculteit2", [0], "1\n")
        self.assertOutputEqual("assignment02_faculteit2", [1], "1\n")
        self.assertOutputEqual("assignment02_faculteit2", [2], "2\n")
        self.assertOutputEqual("assignment02_faculteit2", [3], "6\n")
        self.assertOutputEqual("assignment02_faculteit2", [5], "120\n")

    def test03_faculteit3(self):
        self.assertOutputEqual("assignment03_faculteit3", [-1, 0], "1\n")
        self.assertOutputEqual("assignment03_faculteit3", [-1, -2, 1], "1\n")
        self.assertOutputEqual("assignment03_faculteit3", [-2, -3, -1, 2], "2\n")
        self.assertOutputEqual("assignment03_faculteit3", [-1,-2,-3,-4, 3], "6\n")
        self.assertOutputEqual("assignment03_faculteit3", [-1,-2,-3,-4,-5,5], "120\n")

    def test04_variation(self):
        self.assertOutputEqual("assignment04_variation", [-1, 0], "undefined\n")
        self.assertOutputEqual("assignment04_variation", [0, -1], "undefined\n")
        self.assertOutputEqual("assignment04_variation", [5,5], "120\n")
        self.assertOutputEqual("assignment04_variation", [20,25], "129260083694424883200000\n")

        action_process = Process(target=lambda : self.assertOutputEqual("assignment04_variation", [1,100000], "100000\n"))
        action_process.start()
        action_process.join(timeout=1)

        if action_process.is_alive():
            action_process.terminate()
            self.fail("took to long !")

    def test05_sentinel_extreme_pro(self):
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [0], "0 0\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [1, 0], "1 1\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [-1, 0], "-1 -1\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [-1, 1, 0], "-1 1\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [1, 2, 0], "1 2\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [-1, -2, 0], "-2 -1\n")
        self.assertOutputEqual("assignment05_sentinel_extreme_pro", [1,2,3,4,5,6,7,8,9,10,11,12], "1 10\n")


    def test06_sentinel_armageddon(self):
        self.assertOutputEqual("assignment06_sentinel_armageddon", [0], "0 0\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [1, 0], "1 1\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [-1, 0], "1 1\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [-1, 1, 0], "1 2\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [1, 2, 0], "1 2\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [-1, -2, 0], "2 1\n")
        self.assertOutputEqual("assignment06_sentinel_armageddon", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], "1 10\n")
