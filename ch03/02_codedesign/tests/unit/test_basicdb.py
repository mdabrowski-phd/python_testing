import unittest
from unittest.mock import MagicMock
from pathlib import Path

from todo.db import BasicDB


class TestBasicDB(unittest.TestCase):
    def test_load(self):
        mock_file = MagicMock(read=MagicMock(return_value='["first", "second"]'))
        mock_file.__enter__.return_value = mock_file
        mock_opener = MagicMock(return_value=mock_file)

        db = BasicDB(Path("testdb"), _fileopener=mock_opener)
        loaded = db.load()

        self.assertEqual(loaded, ["first", "second"])
        self.assertEqual(mock_opener.call_args[0][0], Path("testdb"))
        mock_file.read.assert_called_with()
