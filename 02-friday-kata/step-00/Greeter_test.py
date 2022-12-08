import pytest
from Greeter import Greeter

def test_should_say_good_morning():
    greeting = Greeter.say_hello("morning")
    assert greeting == "Good Morning"

def test_should_say_good_night():
    greeting = Greeter.say_hello("night")
    assert greeting == "Good Night"

def test_should_throw_exception():
    with pytest.raises(Exception):
        Greeter.say_hello("boom")