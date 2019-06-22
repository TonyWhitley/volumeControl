# pylint: skip-file
# type: ignore
import unittest
from unittest.mock import patch, call

import status_display

@patch('builtins.print')
class Test_test_status_display(unittest.TestCase):
    def setUp(self):
        self.dispO = status_display.StatusDisplay(['p1','p2','p3'])
    def test_process_not_found(self, mocked_print):
        self.dispO.process_not_found('noSuchProcess')
        assert mocked_print.mock_calls == \
            [call("Warning: process 'noSuchProcess' not running")],\
            mocked_print.mock_calls

if __name__ == '__main__':
    unittest.main()
