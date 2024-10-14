import unittest
from unittest.mock import Mock
import tempfile
from pathlib import Path

from todo.app import TODOApp
from todo.db import BasicDB


class TestRegression(unittest.TestCase):
    def test_os_release(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            app = TODOApp(
                io=(Mock(side_effect=[
                    "add buy milk",
                    'add install "Ubuntu"',
                    "quit"
                    ]), Mock()),
                dbmanager=BasicDB(Path(tmpdirname, "db"))
                )
            app.run()

            restarted_app = TODOApp(
                io=(Mock(side_effect="quit"), Mock()),
                dbmanager=BasicDB(Path(tmpdirname, "db"))
                )
            restarted_app.run()
            