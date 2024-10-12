from unittest.mock import Mock


def read_file(f):
    print("READ FILE CONTENT")
    return f.read()


def main():
    m = Mock()
    read_file(m)

    m.read.return_value = "Hello World!"
    print(read_file(m))

    print(m.read.call_count)

    m.read.assert_called_with()
    m.read.assert_called_with("sample argument")


if __name__ == '__main__':
    main()
