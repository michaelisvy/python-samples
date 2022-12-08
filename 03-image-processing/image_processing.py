import numpy as np
from PIL import Image
import cv2

SRC = 'images/src/'
TARGET = 'images/target/'

def test_shouldBeAPixelBlue():
    array = np.array([[ [10,1,255] ]], dtype=np.uint8)
    print('aab', array)
    img = Image.fromarray(array)
    img.save(TARGET + 'image-blue.png')

def test_shouldBeAPixelGray():
    array = np.array([100], dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(TARGET + 'image-gray.png')

def test_shouldBeAnImage2BlueLine():
    array = np.array([[ [10,1,255],[10,1,255] ]], dtype=np.uint8)
    print('aab', array)
    img = Image.fromarray(array)
    img.save(TARGET + 'image-2blue-line.png')

def test_shouldBeAnImage2BlueColumn():
    array = np.array([[ [10,1,255] ],
                    [ [10,1,255] ]], dtype=np.uint8)
    img = Image.fromarray(array)
    img.save(TARGET + 'image-2blue-column.png')

def test_shouldBeAnImage4Gray():
    array = np.array([ [0,40], [80,255] ], dtype=np.uint8)
    img = Image.fromarray(array)
    print('size', img.size)
    img.save(TARGET + 'image-4gray.png')

def test_shouldResizeImagePIL():
    img = Image.open(SRC + 'sample-high-resolution-image.jpg')
    print('size', img.size)
    img2 = img.resize((1500,1500))
    print('after resize', img2.size)
    img2.save(TARGET + "sample2-pil.jpg")

def test_shouldResizeImageCV2():
    img = cv2.imread(SRC + 'sample-high-resolution-image.jpg')
    print('cv2 size', img.shape)
    img2 = cv2.resize(img, (1500,1500))
    print('after resize', img2.shape)
    cv2.imwrite(TARGET + "sample2-cv2.jpg", img2)

def test_shouldReshapeImageCV2():
    img = cv2.imread(SRC + 'sample-high-resolution-image.jpg')
    print('cv2 size', img.shape)
    img2 = cv2.resize(img, (20,20))
    print('after resize', img2.shape)
    img2.reshape(1,20,20,3)
    cv2.imwrite(TARGET + "sample2-cv2-reshape.jpg", img2)

def test_shouldReshapeImageCV2Gray():
    image = cv2.imread(SRC + 'sample-high-resolution-image.jpg')
    print('cv2 size', image.shape)
    image = cv2.resize(image, (20,20))
    print('after resize', image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image.reshape(1,20,20,1)
    cv2.imwrite(TARGET + "sample2-cv2-reshape.jpg", image)

