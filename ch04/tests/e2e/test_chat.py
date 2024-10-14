import unittest

from chat.client import ChatClient
from chat.server import new_chat_server


class TestChatAcceptance(unittest.TestCase):
    def test_message_exchange(self):
        with new_chat_server():
            user1 = ChatClient("John Doe")
            user2 = ChatClient("Harry Potter")
            user1.send_message("Hello World!")
            messages = user2.fetch_messages()
            assert messages == ["John Doe: Hello World!"]
