import unittest
from unittest import mock

from chat.client import Connection


class TestConnection(unittest.TestCase):
    def test_broadcast(self):
        with mock.patch.object(Connection, "connect"):
            c = Connection(("localhost", 9090))
        
        with mock.patch.object(c, "get_messages", return_value=[]):
            c.broadcast("test message")
            assert c.get_messages()[-1] == "test message"
