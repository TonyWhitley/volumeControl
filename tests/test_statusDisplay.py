import unittest
from unittest.mock import patch, call

import statusDisplay

@patch('builtins.print')
class Test_test_statusDisplay(unittest.TestCase):
    def setUp(self):
        self.dispO = statusDisplay.StatusDisplay(['p1','p2','p3'])
    def test_processNotFound(self, mocked_print):
        self.dispO.processNotFound('noSuchProcess')
        assert mocked_print.mock_calls == \
            [call("Warning: process 'noSuchProcess' not running")],\
            mocked_print.mock_calls

if __name__ == '__main__':
    unittest.main()
