from pytest_bdd import given, when, parsers

from contacts import Application


@given("I have a contact book", target_fixture="contactbook")
def contactbook():
    return Application()


@given(parsers.parse("I have a \"{contactname}\" contact"))
def have_a_contact(contactbook, contactname):
    contactbook.add(contactname, "000")


@when(parsers.parse("I run the \"{command}\" command"))
def runcommand(contactbook, command):
    contactbook.run(command)
