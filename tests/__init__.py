import unittest


if __name__ == '__main__':
    testmodules = [
        'tests.Tester01WarmUp',
        'tests.Tester02Selection',
        'tests.Tester03Iteration',
        'tests.Tester04Arrays',
        'tests.Tester05Allround',
        'tests.Tester06Functions1',
        'tests.Tester06Functions2',
        'tests.Tester06Functions3',
        'tests.Tester06Functions4'
    ]

    suite = unittest.TestSuite()

    for t in testmodules:
        try:
            # If the module defines a suite() function, call it to get the suite.
            mod = __import__(t, globals(), locals(), ['suite'])
            suitefn = getattr(mod, 'suite')
            suite.addTest(suitefn())
        except (ImportError, AttributeError):
            # else, just load all the test cases from the module.
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(t))

    unittest.TextTestRunner().run(suite)