from fizzbuzz import outfizz, outbuzz, endnum


def test_outfizz(capsys):
    outfizz()

    out, _ = capsys.readouterr()
    assert out == "fizz"

def test_outbuzz(capsys):
    outbuzz()

    out, _ = capsys.readouterr()
    assert out == "buzz"
