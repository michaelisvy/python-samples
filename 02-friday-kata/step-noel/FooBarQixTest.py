import pytest
from FooBarQix import FooBarQix

def test_should_return_Foo():
    result = FooBarQix.proceed(3)
    assert result == 3