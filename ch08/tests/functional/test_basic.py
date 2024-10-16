from contacts import Application


class TestBasicFeatures:    
    def test_international_numbers(self):
        app = Application()

        app.run("contacts add NAME +393345554433")

        assert app._contacts == [
            ("NAME", "+393345554433")
        ]

    def test_invalid_strings(self):
        app = Application()

        app.run("contacts add NAME InvalidString")

        assert app._contacts == []


class TestStorage:
    def test_reload(self):
        app = Application()

        app.run("contacts add NAME 3345554433")

        assert app._contacts == [
            ("NAME", "3345554433")
        ]

        app._clear()
        app.load()

        assert app._contacts == [
            ("NAME", "3345554433")
        ]