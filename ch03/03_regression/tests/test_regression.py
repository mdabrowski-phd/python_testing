import unittest
from unittest.mock import Mock
import io

from todo.app import TODOApp
from todo.db import BasicDB


class TestRegression(unittest.TestCase):
    def test_os_release(self):
        fakefile = io.StringIO()
        fakefile.close = Mock()

        app = TODOApp(
            io=(Mock(side_effect=[
                "add buy milk",
                'add install "Ubuntu"',
                "quit"
                ]), Mock()),
            dbmanager=BasicDB(
                None,
                _fileopener=Mock(side_effect=[FileNotFoundError, fakefile]))
            )
        app.run()

        fakefile.seek(0)

        restarted_app = TODOApp(
            io=(Mock(return_value="quit"), Mock()),
            dbmanager=BasicDB(
                None,
                _fileopener=Mock(return_value=fakefile))
            )
        restarted_app.run()
            