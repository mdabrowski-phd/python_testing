import unittest
import tempfile
from pathlib import Path

from todo.app import TODOApp


class TestTODOApp(unittest.TestCase):
    def test_default_dbpath(self):
        app = TODOApp()
        assert Path('.').resolve() == Path(app._dbpath).resolve()

    def test_accepts_dbpath(self):
        expected_path = Path(tempfile.gettempdir(), "anything")
        app = TODOApp(dbpath=str(expected_path))
        assert expected_path == Path(app._dbpath)
