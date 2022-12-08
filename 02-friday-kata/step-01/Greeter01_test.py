import pytest
from Greeter01 import Greeter

def test_should_say_hello():
    assert Greeter.say_hello() == "hello"