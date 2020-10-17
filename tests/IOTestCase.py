import importlib
from unittest import TestCase, mock

import contextlib
from io import StringIO


class IOTestCase(TestCase):

    modules = {}

    def package_name(self):
        return ""

    def import_module(self, module_name):
        package_name = self.package_name()

        if package_name:
            module_name = package_name + "." + module_name

        if module_name in self.modules:
            self.modules[module_name] = importlib.reload(self.modules[module_name])
        else:
            self.modules[module_name] = importlib.import_module(module_name)

    def get_output(self, module_name, input_arr):
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            with mock.patch('builtins.input', side_effect=input_arr):
                self.import_module(module_name)
        return temp_stdout.getvalue()

    def assertOutputEqual(self, module_name, input_arr, expected_output):
        output = self.get_output(module_name, input_arr)
        self.assertEqual(expected_output, output)
