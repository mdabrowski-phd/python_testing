from multiprocessing.managers import SyncManager, ListProxy


def new_chat_server():
    return _ChatServerManager(("", 9090))


class _ChatServerManager(SyncManager):
    def __init__(self, address):
        self._messages = []

        self.register("get_messages", callable=self._srv_get_messages, proxytype=ListProxy)
        super().__init__(address=address, authkey=b'mychatsecret')

    def _srv_get_messages(self):
        return self._messages
