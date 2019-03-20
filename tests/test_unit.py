import unittest
from unittest.mock import patch
import cli

class TestMethods(unittest.TestCase):

    @patch('cli.requests.get')
    def test_get_key_value(self, mock_get):
        mock_get.return_value = "5"
        expected = '5'
        actual = cli.get_key_value('a','5')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()