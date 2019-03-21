import unittest
import click
from click.testing import CliRunner
from cli import get, set, watch, get_key, get_key_value, check_for_update


class TestMethods(unittest.TestCase):

    def test_get_key(self):
        expected = '5'
        actual = get_key('a')
        self.assertEqual(expected, actual)

    def test_get_key_value(self):
        expected = '5'
        actual = get_key_value('a','5')
        self.assertEqual(expected, actual)

    def test_check_for_update(self):
        expected = False
        actual = check_for_update('a','a')
        self.assertEqual(expected, actual)
        expected = True
        actual = check_for_update('a','b')
        self.assertEqual(expected, actual)

    @staticmethod
    def test_get_command():
        runner = CliRunner()
        present = runner.invoke(get, ['a'])
        absent = runner.invoke(get, ['key'])
        assert absent.exit_code == 0
        assert present.exit_code == 0
        assert "This key doesn\'t exist.\nSee store --help for more info on setting keys." in absent.output
        assert "Successfully fetched key: a having value: 5" in present.output


    @staticmethod
    def test_set_command():
        runner = CliRunner()
        result = runner.invoke(set, ['b','6'])
        assert result.exit_code == 0
        assert "Successfully set key: b with value: 6" in result.output

    @staticmethod
    def test_watch_command():
        runner = CliRunner()
        result = runner.invoke(watch, ['key'])
        assert result.exit_code == 0
        assert "This key doesn\'t exist.\nSee store --help for more info on setting keys." in result.output


if __name__ == '__main__':
    unittest.main()