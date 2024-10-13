import pinject


class ChatClient:
    def __init__(self, connection):
        print(self, "GOT", connection)


class Connection:
    pass


class FakeConnection:
    pass


class FakedBindingSpec(pinject.BindingSpec):
    def provide_connection(self):
        return FakeConnection()


class PrototypeBindingSpec(pinject.BindingSpec):
    @pinject.provides(in_scope=pinject.PROTOTYPE)
    def provide_connection(self):
        return Connection()


def main():
    injector = pinject.new_object_graph()
    cli = injector.provide(ChatClient)

    faked_injector = pinject.new_object_graph(binding_specs=[FakedBindingSpec()])
    cli = faked_injector.provide(ChatClient)
    cli2 = faked_injector.provide(ChatClient)

    proto_injector = pinject.new_object_graph(binding_specs=[PrototypeBindingSpec()])
    cli = proto_injector.provide(ChatClient)
    cli2 = proto_injector.provide(ChatClient)


if __name__ == '__main__':
    main()
