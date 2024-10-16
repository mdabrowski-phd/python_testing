from pytest_bdd import scenario, then

from .steps import *


@scenario("features/delete_contact.feature", 
            "Removing a Basic Contact")
def test_deleting_contacts():
    pass


@then("My contacts book is now empty")
def emptylist(contactbook):
    assert contactbook._contacts == []
