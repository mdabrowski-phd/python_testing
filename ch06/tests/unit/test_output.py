import pytest
import fizzbuzz


def test_output(expected_output, capsys):
    func, expected = expected_output

    func()

    out, _ = capsys.readouterr()
    assert out == expected


@pytest.fixture(params=["fizz", "buzz"])
def expected_output(request):
    text = request.param
    if request.config.getoption("--upper"):
        text = text.upper()
    yield getattr(fizzbuzz, f"out{request.param}"), text


@pytest.mark.textcase("lower")
def test_lowercase_output(expected_output, capsys):
    func, expected = expected_output

    func()

    out, _ = capsys.readouterr()
    assert out == expected
    