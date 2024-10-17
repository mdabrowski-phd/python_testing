import pytest
from hypothesis import given
import hypothesis.strategies as st

import contacts.utils
from contacts import Application


@pytest.mark.parametrize("name", ["Mario Alberto Rossi", "Agnès Athénaïs", "吴杨"])
def test_adding_contacts_params(name):
    app = Application()

    app.run(f"contacts add {name} 3456789")
    assert app._contacts == [(name, "3456789")] 


@given(st.text())
def test_adding_contacts(name):
    app = Application()

    app.run(f"contacts add {name} 3456789")

    name = name.strip()
    if name:
        assert app._contacts == [(name, "3456789")] 
    else:
        assert app._contacts == []


@given(a=st.integers(), b=st.integers())
def test_equivalent_sum1_sum2(a: int, b: int) -> None:
    result_sum1 = contacts.utils.sum1(a=a, b=b)
    result_sum2 = contacts.utils.sum2(a=a, b=b)
    assert result_sum1 == result_sum2, (result_sum1, result_sum2)
