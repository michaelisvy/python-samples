import numpy as np
from PIL import Image

def test_shouldBe2Dimensional():
    array = np.array([[1,2],[3,4]])
    
    assert array[0,0] == 1
    assert array[0,1] == 2
    assert array[1,0] == 3
    assert array[1,1] == 4

def test_shouldBe3Dimensional():
    array = np.array([[1,2,3],[4,5,6]])
    
    assert array[0,0] == 1
    assert array[0,2] == 3
    assert array[1,0] == 4
    assert array[1,1] == 5


