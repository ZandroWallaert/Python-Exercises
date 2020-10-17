from tests.IOTestCase import IOTestCase


class Tester04Lists(IOTestCase):

    def package_name(self):
        return "sessions.session04_lists"

    def test01_reverse_sequence_hell(self):
        r = range(0,100)
        self.assertOutputEqual("assignment01_reverse_sequence_hell", r, "\n".join(map(str, reversed(r)))+"\n")

    def test02_highest_frequency(self):
        self.assertOutputEqual("assignment02_highest_frequency", [1, 3, 2, 1, 3, 5, 3, 1, 678], "1\n")
        self.assertOutputEqual("assignment02_highest_frequency", [50, 3, 2, 50, 3, 5, 3, 50, 678], "3\n")
        self.assertOutputEqual("assignment02_highest_frequency", [50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        self.assertOutputEqual("assignment02_highest_frequency", [99, 3, 2, 99, 3, 5, 3, 99, 678], "3\n")
        self.assertOutputEqual("assignment02_highest_frequency", [99, 3, 2, 99, 3, 5,99, 3, 99, 678], "99\n")

        self.assertOutputEqual("assignment02_highest_frequency", [-1], "0\n")

    def test03_highest_frequency2(self):
        self.assertOutputEqual("assignment03_highest_frequency2", [1, 3, 2, 1, 3, 5, 3, 1, 678], "3\n")
        self.assertOutputEqual("assignment03_highest_frequency2", [50, 3, 2, 50, 3, 5, 3, 50, 678], "50\n")
        self.assertOutputEqual("assignment03_highest_frequency2", [50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        self.assertOutputEqual("assignment03_highest_frequency2", [99, 3, 2, 99, 3, 5, 3, 99, 678], "99\n")
        self.assertOutputEqual("assignment03_highest_frequency2", [99, 3, 2, 99, 3, 5,99, 3, 99, 678], "99\n")

        self.assertOutputEqual("assignment03_highest_frequency2", [-1], "0\n")

    def test04_highest_frequency3(self):
        self.assertOutputEqual("assignment04_highest_frequency3", [1, 3, 2, 1, 3, 5, 3, 1, 678], "1 3\n")
        self.assertOutputEqual("assignment04_highest_frequency3", [50, 3, 2, 50, 3, 5, 3, 50, 678], "3 50\n")
        self.assertOutputEqual("assignment04_highest_frequency3", [50, 3, 2, 50, 3, 5, 3, 50, 50, 678], "50\n")
        self.assertOutputEqual("assignment04_highest_frequency3", [99, 3, 2, 99, 3, 5, 3, 99, 678], "3 99\n")
        self.assertOutputEqual("assignment04_highest_frequency3", [99, 3, 2, 99, 3, 5, 99, 3, 99, 678], "99\n")

        self.assertOutputEqual("assignment04_highest_frequency3",
                               [99, 3, 2, 99, 3, 5, 3, 99, 12, 12, 12, 678], "3 12 99\n")

        self.assertOutputEqual("assignment04_highest_frequency3", [-1], "0\n")

    def test05_count_sort(self):
        self.assertOutputEqual("assignment05_count_sort", [3, 2, 1, 3, 5, 3, 1, -10], "[1, 2, 3, 5]\n")

    def test06_count_sort2(self):
        self.assertOutputEqual("assignment06_count_sort2", [3, 2, 1, 5, -10], "[1, 2, 3, 5]\n")
        self.assertOutputEqual("assignment06_count_sort2", [3, 2, 1, 3, 5, 3, 1, -10], "[1, 1, 2, 3, 3, 3, 5]\n")

    def test07_sieve_of_eratosthenes(self):
        self.assertOutputEqual("assignment07_sieve_of_eratosthenes", [14], "2\n3\n5\n7\n11\n13\n")
