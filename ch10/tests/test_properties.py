import pytest

from contacts import Application


@pytest.mark.parametrize("name", ["Mario Alberto Rossi", "Agnès Athénaïs", "吴杨"])
def test_adding_contacts(name):
    app = Application()

    app.run(f"contacts add {name} 3456789")
    assert app._contacts == [(name, "3456789")] 
