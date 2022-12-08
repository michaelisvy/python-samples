from album import Album
import random

def incrementNumber(number):
    return number + 1

def buildSampleArray():
    return [4,3,2,1]

def buildSampleSet():
    return {"my", "guitar", "has", 6, "strings"}

def buildObject():
    return Album("Random Access Memory", "Daft Punk", 2012)

def buildRandomNumber():
    return random.random()


def test_shouldIncrementNumber():
    number = 3
    assert incrementNumber(number) == 4


def test_shouldReturnSampleArray():
    numbers = buildSampleArray()
    print("hiii")
    print(numbers)
    assert numbers[0] == 4
    assert len(numbers) == 4

def test_shouldReturnSampleSet():
    set = buildSampleSet()
    assert "my" in set
    assert len(set) == 5
    # remove one element 
    set.pop()
    assert len(set) == 4

def test_shouldGenerateRandomNumber():
    number = buildRandomNumber()
    assert 0 < number < 1

def test_shouldReturnSampleObject():
    album = buildObject()
    assert album.name == "Random Access Memory"

    