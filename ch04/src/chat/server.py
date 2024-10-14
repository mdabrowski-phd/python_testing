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


class FakeServer:
    def __init__(self):
        self.last_command = None
        self.last_args = None
        self.messages = []

    def __call__(self, *args, **kwargs):
        return self

    def send(self, data):
        callid, command, args, kwargs = data
        self.last_command = command
        self.last_args = args

    def recv(self, *args, **kwargs):
        if self.last_command in ("dummy", "incref", "decref", "accept_connection"):
            return "#RETURN", None
        elif self.last_command == "create":
            return "#RETURN", ("fakeid", tuple())
        elif self.last_command == "append":
            self.messages.append(self.last_args[0])
            return "#RETURN", None
        elif self.last_command == "__getitem__":
            return "#RETURN", self.messages[self.last_args[0]]
        else:
            return "#ERROR", ValueError(f"{self.last_command} - {self.last_args}")

    def close(self):
        pass
