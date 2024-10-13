import unittest
import threading


class TestTODOAcceptance(unittest.TestCase):
    def test_main(self):
        app = TODOApp(io=(self.fake_input, self.fake_output))

        app_thread = threading.Thread(target=app.run, daemon=True)
        app_thread.start()

        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "\n"
            "\n"
            "> "
        ))

        self.send_input("add buy milk")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy milk\n"
            "\n"
            "> "
        ))

        self.send_input("add buy eggs")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy milk\n"
            "2. buy eggs\n"
            "\n"
            "> "
        ))

        self.send_input("del 1")
        welcome = self.get_output()
        self.assertEqual(welcome, (
            "TODOs:\n"
            "1. buy eggs\n"
            "\n"
            "> "
        ))

        self.send_input("quit")
        app_thread.join(timeout=1)
        self.assertEqual(self.get_output(), "Bye\n")
