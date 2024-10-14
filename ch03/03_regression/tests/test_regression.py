import unittest
from unittest.mock import Mock
import io

from todo.db import BasicDB


class TestRegression(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = Mock()

        data = ["add buy milk", 'add install "Ubuntu"', "quit"]
        dbmanager=BasicDB(None, _fileopener=Mock(return_value=fakefile))
        dbmanager.save(data)
        
        fakefile.seek(0)

        loaded_data = dbmanager.load()
        self.assertEqual(loaded_data, data)
            