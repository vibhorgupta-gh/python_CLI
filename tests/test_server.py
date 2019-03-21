import unittest
from server import get, set


class TestServerMethods(unittest.TestCase):

    def test_set(self):
        expected = 'value'
        actual = str(set('key','value'))
        actual = actual.split('\'')
        actual = actual[0]
        self.assertEqual(expected, actual)

    def test_get(self):
        expected = 'value'
        actual = str(get('key'))
        actual = actual.split('\'')
        actual = actual[1]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()