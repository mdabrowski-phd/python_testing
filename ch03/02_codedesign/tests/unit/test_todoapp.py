import unittest
import tempfile
from pathlib import Path
from unittest.mock import Mock

from todo.app import TODOApp


class TestTODOApp(unittest.TestCase):
    def test_default_dbpath(self):
        app = TODOApp()
        assert Path('.').resolve() == Path(app._dbpath).resolve()

    def test_accepts_dbpath(self):
        expected_path = Path(tempfile.gettempdir(), "anything")
        app = TODOApp(dbpath=str(expected_path))
        assert expected_path == Path(app._dbpath)

    def test_load(self):
        dbpath = Path(tempfile.gettempdir(), "anything")
        dbmanager = Mock(load=Mock(return_value=["buy milk", "buy water"]))
        app = TODOApp(
            io=(Mock(return_value="quit"), Mock()),
            dbpath=dbpath,
            dbmanager=dbmanager
            )
        app.run()

        dbmanager.load.assert_called_with(dbpath)
        assert app._entries == ["buy milk", "buy water"]
