import functools


class TODOApp:
    def __init__(self,
                 io=(input, functools.partial(print, end="")),
                 dbmanager=None):
        self._in, self._out = io
        self._quit = False
        self._entries = []
        self._dbmanager = dbmanager

    def run(self):
        if self._dbmanager is not None:
            self._entries = self._dbmanager.load()

        self._quit = False
        while not self._quit:
            self._out(self.prompt(self.items_list()))
            command = self._in()
            self._dispatch(command)

        if self._dbmanager is not None:
            self._dbmanager.save(self._entries)
        self._out("Bye!\n")

    def items_list(self):
        enumerated_items = enumerate(self._entries, start=1)
        return '\n'.join([f"{idx}. {entry}" for idx, entry in enumerated_items])

    def prompt(self, output):
        return f"TODOs:\n{output}\n\n> "
    
    def _dispatch(self, cmd):
        cmd, *args = cmd.split(" ", 1)
        executor = getattr(self, f"cmd_{cmd}", None)
        if executor is None:
            self._out(f"Invalid command: {cmd}\n")
            return
        executor(*args)

    def cmd_quit(self, *_):
        self._quit = True

    def cmd_add(self, what):
        self._entries.append(what)

    def cmd_del(self, idx):
        idx = int(idx) - 1
        if not 0 <= idx < len(self._entries):
            self._out("Invalid index\n")
            return
        self._entries.pop(idx)
