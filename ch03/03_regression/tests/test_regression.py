import unittest
import threading
import queue
import tempfile
from pathlib import Path

from todo.app import TODOApp
from todo.db import BasicDB


class TestRegression(unittest.TestCase):
    def setUp(self):
        self.outputs = queue.Queue()
        self.inputs = queue.Queue()
        
        self.fake_output = lambda txt: self.outputs.put(txt)
        self.fake_input = lambda: self.inputs.get()

        self.get_output = lambda: self.outputs.get(timeout=1)
        self.send_input = lambda cmd: self.inputs.put(cmd)

    def create_thread(self, dirname):
        return threading.Thread(
            target=TODOApp(
                io=(self.fake_input, self.fake_output),
                dbmanager=BasicDB(Path(dirname, "db"))
                ).run,
                daemon=True)

    def test_os_release(self):
        with tempfile.TemporaryDirectory() as tmpdirname:
            app_thread = self.create_thread(tmpdirname)
            app_thread.start()
            self.get_output()
            
            self.send_input("add buy milk")
            self.send_input('add install "Ubuntu"')
            self.send_input("quit")
            app_thread.join(timeout=1)

            while True:
                try:
                    self.get_output()
                except queue.Empty:
                    break

            app_thread = self.create_thread(tmpdirname)
            app_thread.start()
            self.get_output()
