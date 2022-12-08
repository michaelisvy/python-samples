import pytest
from FooBarQix import FooBarQix

def test_should_say_hello_morning():
    assert FooBarQix.say_hello("morning") == "Good Morning"

def test_should_say_hello_night():
    assert FooBarQix.say_hello("night") == "Good Night"

def test_should_throw_exception():
    with pytest.raises(Exception):
        FooBarQix.say_hello("boom")